# Linda: Composición de Canciones V.3

Linda es un programa en Python diseñado para ayudar en la composición de canciones. Este script permite seleccionar un tono base y generar una secuencia de acordes en función de la tonalidad (mayor o menor) y el número de tonos deseado.

## Contenido del Script

El script realiza las siguientes tareas:

- Definición de Notas: Lista de notas musicales en el sistema de doce tonos.
- Saludo Inicial: Imprime un saludo.
- Función para Desplazar Notas: desplazar_nota_y_reordenar(notas, nota). Esta función toma una nota base y reorganiza la lista de notas a partir de la nota seleccionada.
- Selección del Tono Base: El usuario selecciona el tono en el que desea componer.
- Selección de la Tonalidad: El usuario selecciona si quiere comenzar en tono mayor o menor.
- Generación de Secuencia de Acordes: Basado en la tonalidad y el número de tonos seleccionados, el programa sugiere una secuencia de acordes.

## Uso del Script

Requisitos

- Python 3.x

## Instrucciones

Ejecutar el Script: Ejecuta el script en un entorno de Python.
Interacción con el Usuario:

- Selecciona el tono base en el que deseas componer tu canción (por ejemplo, C, D#, G, etc.).
- Elige la tonalidad en la que quieres comenzar (MAYOR o MENOR).
- Indica el número de tonos que deseas para la composición (4 u 8 tonos).

### Ejemplo de Ejecución

```python
python main.py
```

### Ejemplo de Salida

```bash
['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
Selecciona el tono en el que deseas componer tu cancion: G
En que tono quieres comenzar MAYOR o MENOR: mayor
Cuantos tono quieres que lleve la cancion: 4
Podrias usar esta secuencia de acordes:
G, Dm, Am, C#
```

## Notas

Asegúrate de ingresar un tono válido y seleccionar la tonalidad correcta para obtener resultados precisos.
El programa actualmente soporta secuencias de 4 u 8 tonos únicamente. No se permiten compases incompletos.
