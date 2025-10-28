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

#act 5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg_rest = segundos % 60
    return f"{horas:02}h:{minutos:02}m:{seg_rest:02}s"

#act 6
def tabla_multiplicar(num):
    print(f"Tabla de multiplicar de {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

#act 7
def operaciones_basicass(a, b):
    resul = (f"{a} + {b} ={a+b}, {a} - {b} ={a-b}, {a} * {b} ={a*b}, {a} / {b} ={a//b}")
    return resul

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

segundos = int(input("Ingrese los segundos que se transformaran a horas "))
print(f"los {segundos} ssegundos se transformaro en {segundos_a_horas(segundos)}")

num = int(input("ingree un numero para hacer la tabla de multiplicar "))
tabla_multiplicar(num)

a = int(input("ingrese el valor de a para las operaciones "))
b = int(input("Ingrese el valor de b para las operaciones "))
print(operaciones_basicass(a,b))