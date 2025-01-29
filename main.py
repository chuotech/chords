# import pretty_midi

# def extract_notes_from_midi(midi_file):
#     # Load the MIDI file
#     midi_data = pretty_midi.PrettyMIDI(midi_file)
    
#     # Get all notes in the MIDI file
#     notes = []
#     for instrument in midi_data.instruments:
#         for note in instrument.notes:
#             notes.append(note.pitch)
    
#     return notes

# def infer_key_signature(midi_file):
#     # Extract the notes from the MIDI file
#     notes = extract_notes_from_midi(midi_file)
    
#     # Map the notes to their pitch classes (0-11, representing C, C#, D, ..., B)
#     pitch_classes = [note % 12 for note in notes]
    
#     # Manually count the frequency of each pitch class (note)
#     pitch_class_counts = {}
#     for pitch_class in pitch_classes:
#         if pitch_class in pitch_class_counts:
#             pitch_class_counts[pitch_class] += 1
#         else:
#             pitch_class_counts[pitch_class] = 1
    
#     # Sort the pitch classes by their frequency (most common first)
#     sorted_pitch_classes = sorted(pitch_class_counts.items(), key=lambda x: x[1], reverse=True)
    
#     # Map pitch classes to their corresponding note names
#     pitch_class_to_name = {
#         0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 
#         9: 'A', 10: 'A#', 11: 'B'
#     }
    
#     # Extract the most common notes
#     most_common_notes = [pitch_class_to_name[pitch_class] for pitch_class, count in sorted_pitch_classes]
    
#     print("Most common pitch classes:", sorted_pitch_classes)
#     print("Corresponding notes:", most_common_notes)
    
#     # Return the most common notes as the inferred key signature
#     return most_common_notes

# # Example usage
# midi_file = 'morefight.mid'  # Replace with your MIDI file path
# key_signature = infer_key_signature(midi_file)

# print("Inferred Key Signature:", key_signature)
from music21 import converter, chord

def get_key_signature(midi_file):
    # Load the MIDI file into a music21 stream
    midi_stream = converter.parse(midi_file)
    
    # Analyze the key signature of the stream
    key_signature = midi_stream.analyze('key')
    
    return key_signature

def get_chords(midi_file):
    chords = []
    midi_stream = converter.parse(midi_file)
    for element in midi_stream.recurse().notes:
        if isinstance(element, chord.Chord):
            chords.append(element)
    
    for c in chords:
        print(c.pitchedCommonName)
    
# Example usage
midi_file = 'major1.mid'  # Replace with the path to your MIDI file
key_signature = get_key_signature(midi_file)

print("Detected Key Signature:", key_signature)
get_chords(midi_file)