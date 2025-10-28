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
