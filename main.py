#Linda es un programa que ayuda a la composicion de una cancion V.1
notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
print("Hola", "Pvto", sep=" ")

def desplazar_nota_y_reordenar(notas, nota):
    if nota in notas:
        indice = notas.index(nota)
        nueva_lista = notas[indice:] + notas[:indice]
        return nueva_lista
    else:
        return "Nota no valida"

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
    elif (tempo == 8):
        print("Podrias usar esta secuencia de acordes: ")
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], nueva_lista[8], nueva_lista[2], nueva_lista[7], sep=", ")
    else:
        print("No puedes elejir compases incompletos D:")
else:
    nueva_lista[0]+="m"
    nueva_lista[5]+="m"
    nueva_lista[7]+="7"
    tempo = int(input("Cuantos tono quieres que lleve la cancion: "))
    if (tempo == 4):
    #
        print("Podrias usar esta secuencia de acordes: ")
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], sep=", ")
    elif (tempo == 8):
        
        print("Podrias usar esta secuencia de acordes: ")
        print(nueva_lista[0], nueva_lista[5], nueva_lista[10], nueva_lista[3], nueva_lista[8], nueva_lista[2], nueva_lista[7], sep=", ")
    else:
        print("No puedes elejir compases incompletos D:")