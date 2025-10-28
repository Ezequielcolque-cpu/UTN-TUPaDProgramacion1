#print("Hello Wordl")
import math

#act1
def imprimir_hola_mundo():
    return "Hello Wordl"

#act2
def Saludo_usuario(nom):
    return f"Hola {nom}, como te va?"

#act3
def info_personal(nom,apell,edad,resid):
    return f"Hola {nom} {apell}, de {edad} años de {resid}"

#act4
def calcular_area_circulos(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulos(radio):
    return 2 * math.pi * radio

#main program
print(imprimir_hola_mundo())

nom = input("ingrese un nombre ")
print(Saludo_usuario(nom))

nom = input("ingrese un nombre ")
apell = input("ingrese un apellido ")
edad =int(input("Ingrese ssu edad "))
resid = input("ingrese un residencia ")
print(info_personal(nom, apell, edad, resid))

radio =int(input("Ingresse el radio del circulo "))
print(f"El area del circulo es de {calcular_area_circulos(radio)}cm y su perimetro es de {calcular_perimetro_circulos(radio)}cm")