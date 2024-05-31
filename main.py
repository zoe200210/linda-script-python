import pygame
import os

#Linda es un programa que ayuda a la composicion de una cancion V.3

def desplazar_nota_y_reordenar(notas, nota):
    if nota in notas:
        indice = notas.index(nota)
        nueva_lista = notas[indice:] + notas[:indice]
        return nueva_lista
    else:
        return "Nota no valida"

def sonido(nueva_lista):
    # Inicializa pygame mixer
    pygame.mixer.init()

    # Base directory where the note files are located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # A dictionary to map notes to their corresponding audio file paths
    note_files = {
        #mayores
        "C": os.path.join(base_dir, "piano_chords/C.wav"),
        "D": os.path.join(base_dir, "piano_chords/D.wav"),
        "E": os.path.join(base_dir, "piano_chords/E.wav"),
        "F": os.path.join(base_dir, "piano_chords/F.wav"),
        "G": os.path.join(base_dir, "piano_chords/G.wav"),
        "A": os.path.join(base_dir, "piano_chords/A.wav"),
        "B": os.path.join(base_dir, "piano_chords/B.wav"),
        #menores
        "Cm": os.path.join(base_dir, "piano_chords/Cm.wav"),
        "Dm": os.path.join(base_dir, "piano_chords/Dm.wav"),
        "Em": os.path.join(base_dir, "piano_chords/Em.wav"),
        "Fm": os.path.join(base_dir, "piano_chords/Fm.wav"),
        "Gm": os.path.join(base_dir, "piano_chords/Gm.wav"),
        "Am": os.path.join(base_dir, "piano_chords/Am.wav"),
        "Bm": os.path.join(base_dir, "piano_chords/Bm.wav"),
        #sostenidos_mayores
        "C#": os.path.join(base_dir, "piano_chords/C#.wav"),
        "D#": os.path.join(base_dir, "piano_chords/D#.wav"),
        "F#": os.path.join(base_dir, "piano_chords/F#.wav"),
        "G#": os.path.join(base_dir, "piano_chords/G#.wav"),
        "A#": os.path.join(base_dir, "piano_chords/A#.wav"),
        #sostenidos_menores
        "C#m": os.path.join(base_dir, "piano_chords/C#m.wav"),
        "D#m": os.path.join(base_dir, "piano_chords/D#m.wav"),
        "F#m": os.path.join(base_dir, "piano_chords/F#m.wav"),
        "G#m": os.path.join(base_dir, "piano_chords/G#m.wav"),
        "A#m": os.path.join(base_dir, "piano_chords/A#m.wav"),
        #septimas
        "C7": os.path.join(base_dir, "piano_chords/C7.wav"),
        "D7": os.path.join(base_dir, "piano_chords/D7.wav"),
        "E7": os.path.join(base_dir, "piano_chords/E7.wav"),
        "F7": os.path.join(base_dir, "piano_chords/F7.wav"),
        "G7": os.path.join(base_dir, "piano_chords/G7.wav"),
        "A7": os.path.join(base_dir, "piano_chords/A7.wav"),
        "B7": os.path.join(base_dir, "piano_chords/B7.wav"),
        #sostenidos_mayores_septima
        "C#7": os.path.join(base_dir, "piano_chords/C#7.wav"),
        "D#7": os.path.join(base_dir, "piano_chords/D#7.wav"),
        "F#7": os.path.join(base_dir, "piano_chords/F#7.wav"),
        "G#7": os.path.join(base_dir, "piano_chords/G#7.wav"),
        "A#7": os.path.join(base_dir, "piano_chords/A#7.wav"),
        #sostenidos_menores_septima
        "C#m7": os.path.join(base_dir, "piano_chords/C#m7.wav"),
        "D#m7": os.path.join(base_dir, "piano_chords/D#m7.wav"),
        "F#m7": os.path.join(base_dir, "piano_chords/F#m7.wav"),
        "G#m7": os.path.join(base_dir, "piano_chords/G#m7.wav"),
        "A#m7": os.path.join(base_dir, "piano_chords/A#m7.wav"),
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
    notes_to_play = nueva_lista

    # Play each note
    for note in notes_to_play:
        play_note_with_pygame(note)
    
notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
print(notas)
nota_a_desplazar = str(input("Selecciona el tono en el que deseas componer tu cancion: ")).upper()
nueva_lista = desplazar_nota_y_reordenar(notas, nota_a_desplazar)

mayor_menor = str(input("En que tono quieres comenzar MAYOR o MENOR: ")).lower()

if (mayor_menor == "mayor"):
    nueva_lista[5]+="m"
    
    tempo = int(input("Cuantos tono quieres que lleve la cancion: "))
    if (tempo == 4):
    #
        print("Podrias usar esta secuencia de acordes: ")
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], sep=", ")
        indices = [0, 5, 10, 3]
        sonidos = [nueva_lista[i] for i in indices]
        sonido(sonidos)
    elif (tempo == 8):
        print("Podrias usar esta secuencia de acordes: ")
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], nueva_lista[8], nueva_lista[2], nueva_lista[7], sep=", ")
        indices = [0, 5, 10, 3, 8, 2, 7]
        sonidos = [nueva_lista[i] for i in indices]
        sonido(sonidos)
    else:
        print("No puedes elejir compases incompletos D:")
        
elif (mayor_menor == "menor"):
    
    tempo = int(input("Cuantos tono quieres que lleve la cancion: "))
    if (tempo == 4):
        
        print("Podrias usar esta secuencia de acordes: ")
        nueva_lista[0]+="m"
        nueva_lista[5]+="m"
        nueva_lista[3]+="7"
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], sep=", ")
        indices = [0, 5, 10, 3]
        sonidos = [nueva_lista[i] for i in indices]
        sonido(sonidos)
        
    elif (tempo == 8):
            
        print("Podrias usar esta secuencia de acordes: ")
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], nueva_lista[8], nueva_lista[2], nueva_lista[7], sep=", ")
        indices = [0, 5, 10, 3, 8, 2, 7]
        sonidos = [nueva_lista[i] for i in indices]
        sonido(sonidos)
    else:
            print("No puedes elejir compases incompletos")