#print("Hello World")
#act1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300
print(precios_frutas)
#act 2
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
#act 3
lista_fruta=['Banan','Anana','Melon','Uva','Manzana','Naranja','Pera']
print(lista_fruta)
#act 4
contactos = {}
print("Ingrese 5 contactos telefonicos")
for  i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numeroT =input(f"Ingrese el numero telefonico de {nombre}: ")
    contactos[nombre]=numeroT
    print() #Linea en blanco
nombre_a_busscar = input("Ingrese el nombre de contacto a buscar: ")
if nombre_a_busscar in contactos:
    print(f"El contacto {nombre_a_busscar} es {contactos[nombre_a_busscar]}")
else:
    print(f"No se encontro ningun contacto con el nombre de {nombre_a_busscar}")
#act 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
repeticiones = {}
for palabra in palabras:
    if palabra in repeticiones:
        repeticiones[palabra] += 1
    else:
        repeticiones[palabra] =1
print(f"Palabras unicas:{palabras_unicas}")
print(f"Repeticion de palabras: {repeticiones}")
#act6
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    print(f"Ingrese lass notas de {nombre}")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    alumnos[nombre]=(nota1,nota2,nota3)
    print()#Linea en blanco
print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
#act 7
parcial1 = {"Ana", "Juan", "Pedro", "Lucía"}
parcial2 = {"Juan", "María", "Pedro", "Sofía"}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)
#act 8
stock ={'manzanas':10, 'peras': 6, 'naranjas': 12}
print("Inventario actual: ")
for producto, cantidad in stock.items():
    print(f"{producto}:{cantidad} unidades")
print("\n--- Conssulta / Actualizacion de Stock ---")
producto = input("Ingrese el nombre del producto: ").lower()
if producto in stock:
    print(f"El stock actual de '{producto}' es {stock[producto]} unidades")
    agregar = input("¿Desea agregar unidades a este producto? (s/n)").lower()
    if agregar == "s":
        cantidad = int(input("Ingrese cuantass unidades desea agregar: "))
        stock[producto]+=cantidad
        print(f"Nuevo stock {producto}: {stock[producto]} unidades")
    else:
        print("No se modifico el stock")
else:
    print(f"El producto '{producto}' no existe")
    agregar_nuevo = input("¿Desea agregarlo al inventario? (s/n)").lower()
    if agregar_nuevo == "s":
        cantidad = int(input("Ingrese la cantidad inicial del stock: "))
        stock[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades")
    else:
        print("No se agregó el producto")
print("\nInventario final:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad} unidades")
#act 9
agenda = {}
print("Cargá tus eventos en la agenda:")
for i in range(3):
    dia = input("Ingrese el día: ")
    hora = input("Ingrese la hora (por ejemplo, 14:00): ")
    evento = input("Ingrese el evento: ")
    
    clave = (dia, hora)  # tupla (día, hora)
    agenda[clave] = evento
    print()  # línea en blanco
print("Agenda completa:")
for clave, evento in agenda.items():
    print(f"Día: {clave[0]}, Hora: {clave[1]} → {evento}")
print()
dia_buscar = input("Ingrese el día a consultar: ")
hora_buscar = input("Ingrese la hora a consultar: ")
clave_buscar = (dia_buscar, hora_buscar)
if clave_buscar in agenda:
    print(f"Evento encontrado: {agenda[clave_buscar]}")
else:
    print("No hay eventos en ese día y hora.")
#act 10
paises = {"Argentina": "Buenos Aires","Chile": "Santiago","Perú": "Lima","Brasil": "Brasilia","Uruguay": "Montevideo"}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario original (País → Capital):")
print(paises)
print("\nDiccionario invertido (Capital → País):")
print(capitales)
