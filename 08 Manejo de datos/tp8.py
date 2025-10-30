# 1. Crear archivo inicial con productos (solo si no existe)
import os

archivo = "08 Manejo de datos/productos.txt"

if not os.path.exists(archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,450.0,15\n")
        f.write("Goma,80.0,50\n")
    print("Archivo 'productos.txt' creado con productos iniciales.\n")

# 2. Leer y mostrar productos
productos = []
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

print("Productos actuales:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# 3. Agregar producto desde teclado
print("\n¿Querés agregar un nuevo producto?")
nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

# Agregar a la lista
productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

# 4. Buscar producto por nombre
buscar = input("\nIngresá el nombre del producto a buscar: ")
encontrado = False

for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"\nProducto encontrado:\nNombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nProducto no encontrado.")

# 5. Guardar productos actualizados
with open(archivo, "w", encoding="utf-8") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo actualizado con todos los productos.")
