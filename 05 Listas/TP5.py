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
