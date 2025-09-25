import math
import random
#actividad 1
notas = [7, 8, 9, 6, 10, 5, 8, 9, 7, 6]
print("Lista completa de notas:", notas)
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#Actividad 2
productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)
print("Lista ordenada:", sorted(productos))
eliminar = input("Ingrese el producto a eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
print("Lista actualizada:", sorted(productos))

#Actividad 3
numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista completa:", numeros)
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Números pares:", pares, "Cantidad:", len(pares))
print("Números impares:", impares, "Cantidad:", len(impares))

#Actividad 4
Datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
srepe = list(set(Datos))
print("Lista sin repetidos:", srepe)

#Actividad 5
estudiantes = ["Mario", "Luigi", "María", "Facundo", "Daniela", "Kirby", "Lucia", "Diego"]
accion = input("Desea agregar o eliminar un estudiante? (agregar/eliminar): ").lower()
if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
print("Lista final de estudiantes:", estudiantes)

#Actividad 6
numeros = [1, 2, 3, 4, 5, 6, 7]
rotada = [numeros[-1]] + numeros[:-1]
print("Lista rotada:", rotada)

#Actividad 7
temperaturas = [
    [15, 25], [17, 28], [16, 27], [14, 26],
    [18, 30], [19, 31], [17, 29]
]
minimas = [t[0] for t in temperaturas]
maximas = [t[1] for t in temperaturas]
print("Promedio mínima:", sum(minimas)/len(minimas))
print("Promedio máxima:", sum(maximas)/len(maximas))
amplitudes = [t[1] - t[0] for t in temperaturas]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1
print("Día con mayor amplitud térmica:", dia_mayor_amplitud)

#actividad 8
notas = [
    [7, 8, 9],
    [6, 7, 8],
    [9, 8, 7],
    [5, 6, 7],
    [8, 9, 10]
]
for i, estudiante in enumerate(notas, start=1):
    print(f"Promedio estudiante {i}:", sum(estudiante)/len(estudiante))
for j in range(3):
    materia = [notas[i][j] for i in range(5)]
    print(f"Promedio materia {j+1}:", sum(materia)/len(materia))

#Actividad 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
for turno in range(9):
    for fila in tablero:
        print(" ".join(fila))
    print()
    jugador = "X" if turno % 2 == 0 else "O"
    fila = int(input(f"Jugador {jugador}, ingrese fila (0-2): "))
    columna = int(input(f"Jugador {jugador}, ingrese columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, intente de nuevo")
        turno -= 1

#Actividad 10
ventas = [
    [5, 3, 4, 2, 1, 3, 2],
    [2, 4, 3, 5, 2, 3, 4],
    [3, 5, 2, 4, 3, 2, 1],
    [4, 2, 3, 5, 4, 3, 2]
]
for i, producto in enumerate(ventas, start=1):
    print(f"Total vendido producto {i}:", sum(producto))
totales_dia = [sum(ventas[p][d] for p in range(4)) for d in range(7)]
dia_max = totales_dia.index(max(totales_dia)) + 1
print("Día con mayores ventas:", dia_max)
totales_productos = [sum(p) for p in ventas]
producto_max = totales_productos.index(max(totales_productos)) + 1
print("Producto más vendido:", producto_max)
