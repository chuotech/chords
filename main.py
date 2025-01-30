from music21 import converter, chord
import time
import pretty_midi
def get_notes(midi_file_pm):
    notes = []
    for instrument in midi_file_pm.instruments:
        for note in instrument.notes:
            notes.append({"pitch": note.pitch, "onset": note.start, "offset": note.end})
    return notes
def get_key_signature(midi_stream):
    # Load the MIDI file into a music21 stream
    # Analyze the key signature of the stream
    key_signature = midi_stream.analyze('key')
    
    return key_signature

def get_chords(midi_stream):
    chords = []
    for element in midi_stream.recurse().notes:
        if isinstance(element, chord.Chord):
            chords.append(element)
    
    for c in chords:
        print(str(c)+" ~~ "+str(c.pitchedCommonName))

# def get_chord()
def get_etimated_tempo(midi_file_pm):
    tempo_changes = midi_file_pm.get_tempo_changes()
    if len(tempo_changes[0]) > 0:
        tempo = tempo_changes[1][0]
        print(f"Tempo: {tempo} BPM")
        return tempo
    else:
        print("No tempo found")
        return
# def strum_pattern(midi_stream):
start = time.time()
midi_file = 'major1.mid'  # Replace with the path to your MIDI file
midi_file_pm = pretty_midi.PrettyMIDI(midi_file)
midi_stream = converter.parse(midi_file)
midi_notes = get_notes(midi_file_pm)
key_signature = get_key_signature(midi_stream)
end = time.time()
print("Detected Key Signature:", key_signature)
get_chords(midi_stream)
get_etimated_tempo(midi_file_pm)
print(str(end - start)+" secs")
