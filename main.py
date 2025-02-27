from music21 import converter, chord
import time
import pretty_midi
import pprint

class MIDI_Stream:
    def __init__(self, midi_file, tempo = None):
        self.midi_file = midi_file
        self.tempo = tempo
        self.midi_stream = pretty_midi.PrettyMIDI(midi_file)
        self.duration = round(self.midi_stream.get_end_time())
        if (tempo == None):
            self.tempo = self.get_tempo()
        self.min_length = 60 / self.tempo / 8
        self.notes = self.get_notes()
        self.notes = self.connect_notes()
        print(str(self.min_length) + " minimun length")

    def get_tempo(self):
        tempo_changes = self.midi_stream.get_tempo_changes()
        if len(tempo_changes[0]) > 0:
            tempo = tempo_changes[1][0]
            print(f"Tempo: {tempo} BPM")
            return tempo
        else:
            print("No tempo found")
            return
    
    def get_notes(self):
        notes = []
        for instrument in self.midi_stream.instruments:
            for note in instrument.notes:
                if (round(note.end, 5) - round(note.start, 5) >= self.min_length):
                    notes.append({"pitch": note.pitch, "onset": round(note.start, 5), "offset": round(note.end, 5)})
        pprint.pp(notes)
        return notes
    
    def connect_notes(self):
        curr_note = self.notes[0]
        for i in range(len(self.notes)):
            j = i + 1
            while j < len(self.notes):
                if self.notes[i]["offset"] == self.notes[j]["onset"]:
                    curr_note = self.notes[i]
                    self.notes[i] = {"pitch": curr_note["pitch"], "onset": curr_note["onset"], "offset": self.notes[j]["offset"]}
                    self.notes.pop(j)
                    break
                if self.notes[j]["offset"] == self.notes[i]["onset"]:
                    curr_note = self.notes[j]
                    self.notes[j] = {"pitch": curr_note["pitch"], "onset": self.notes[j]["onset"], "offset": curr_note["offset"]}
                    self.notes.pop(i)
                    break
                j = j + 1
            j = 0
        pprint.pp(self.notes)
        return self.notes


    def get_full_chord_list(self):
        print(self.duration)
        beats_total = int((self.tempo/60)*self.duration *2)
        quarter_length = 60 / self.tempo
        eighth_length = quarter_length / 2
        thirty_second = eighth_length/4

        # notes = self.get_notes()
        # print(beats_total)
        chord_list = []
        # curr_note = notes[0]
        curr_highest_pitch = 0
        curr_lowest_pitch = 10000
        curr_chord = []
        curr_highest = 0
        curr_lowest = 100000
        # curr_min_interval_length = -thirty_second
        curr_max_interval_length = eighth_length - thirty_second
        print(curr_max_interval_length)
        i = 0
        for interval in range(beats_total):
            while i < len(self.notes) and (self.notes[i]["onset"] <= curr_max_interval_length):
                curr_chord.append(self.notes[i]["pitch"])
                if self.notes[i]["pitch"] >= curr_highest_pitch:
                    curr_highest = self.notes[i]["onset"]
                    curr_highest_pitch = self.notes[i]["pitch"]
                if self.notes[i]["pitch"] <= curr_lowest_pitch:
                    curr_lowest = self.notes[i]["onset"]
                    curr_lowest_pitch = self.notes[i]["pitch"]
                i += 1
            # if (len(curr_chord) > 1):
            chord_list.append((chord.Chord(curr_chord).pitchedCommonName, "eighth note "+str(interval + 1), str(self.get_strum(curr_lowest, curr_highest))))
            # prev_chord = chord.Chord(curr_chord).pitchedCommonName
            curr_max_interval_length += eighth_length
            curr_lowest = 0
            curr_highest = 0
            if i < len(self.notes) and curr_max_interval_length >= self.notes[i]["onset"]:
                curr_chord = []
                curr_highest = 0
                curr_lowest = 100000
                curr_highest_pitch = 0
                curr_lowest_pitch = 10000
        pprint.pp(chord_list) #remove for lactency
        return chord_list
    
    def get_strum(self, lowest, highest):
        if highest > lowest:
            return "DOWN"
        elif lowest > highest:
            return "UP"
        else:
            return "HOLD"
    # def get_intervals(self):
    #     interval_list = []
        

start = time.time()
midi_path = "split.mid"
midi_stream = MIDI_Stream(midi_path)
chords = midi_stream.get_full_chord_list()
end = time.time()
print(end - start)
