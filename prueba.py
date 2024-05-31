import pygame
import os

# Inicializa pygame mixer
pygame.mixer.init()

# Base directory where the note files are located
base_dir = os.path.dirname(os.path.abspath(__file__))

# A dictionary to map notes to their corresponding audio file paths
note_files = {
    "C": os.path.join(base_dir, "piano_notes/C.wav"),
    "D": os.path.join(base_dir, "piano_notes/D.wav"),
    "E": os.path.join(base_dir, "piano_notes/E.wav"),
    "F": os.path.join(base_dir, "piano_notes/F.wav"),
    "G": os.path.join(base_dir, "piano_notes/G.wav"),
    "A": os.path.join(base_dir, "piano_notes/A.wav"),
    "B": os.path.join(base_dir, "piano_notes/B.wav"),
    # Add paths for other notes as needed
}

def play_note_with_pygame(note):
    if note in note_files:
        file_path = note_files[note]
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Espera hasta que termine de reproducir
                pygame.time.Clock().tick(10)
        else:
            print(f"File {file_path} not found.")
    else:
        print(f"Note {note} not found in note_files dictionary.")

# Notes you want to play
notes_to_play = ["A", "G", "F"]

# Play each note
for note in notes_to_play:
    play_note_with_pygame(note)
