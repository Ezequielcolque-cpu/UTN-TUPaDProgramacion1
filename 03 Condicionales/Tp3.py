import math
import random
from statistics import mode, median, mean
print ("Hola")
#Activida 1 y 4
Edad = int (input ("Me podrías decir tu edad por favor "))
if Edad < 12:
    print (f"Usted es un niñ@ de {Edad} años")
elif Edad < 18:
    print(f"Usted es un adolecente de {Edad} años")
elif Edad < 30:
    print(f"Usted es mayor de edad, un adult@ joven de {Edad} años")
elif Edad < 60:
    print(f"Usted es un adult@ de {Edad} años")
else :
    print(f"Usted es una persona mayor/abuel@ de {Edad} años")
#Actividad 2
print("Ahora veremos si quedas aprobado o no")
Nota = float (input("Ingrese su nota: "))
RedondeoR = (input("Desea aplicar redondeos? (Si/No) ")).strip().lower()
Verdadero = (RedondeoR == "si")
if Verdadero:
    Redondeado = round(Nota)
    if Redondeado < 6:
        print(f"Usted esta Desaprobado, su nota fue de {Redondeado} redondeado")
    else:
        print(f"Usted esta Aprobado, su nota fue de {Redondeado} redondeado")
else:
    if Nota < 6:
        print(f"Usted esta Desaprobado, su nota fue de {Nota}")
    else:
        print(f"Usted esta Aprobado, su nota fue de {Nota}")
#Actividad 3
Num1 = int(input("Ingrese un numero par: "))
while True:
    if Num1 % 2 == 0:
        print("Ha ingresado un numero par")
        break
    else:
        print(f"Por favor, ingrese un numero par, {Num1} no es par")
    Num1 = int(input("Ingrese un numero par: "))
#Actividad 5
Clave = input("Ingrese una contraseña (8-14 caracteres) ")
while True:
    if len(Clave) >= 8 and len(Clave) <= 14:
        print("Ha ingresado una contraseña correcta")
        break
    else:
        print(f"Por favor, ingrese una contraseña de entre 8 a 14 caracteres, su contraseña tiene {len(Clave)} caracteres")
    Clave = int(input("Ingrese una contraseña (8-14 caracteres) "))
#Actividad 6
print("Ahora determinaremos el sesgo de 50 numeros aleatorios")
Numeros_aleatorios = [random.randint (1, 100) for i in range (50)]
print(f"Los numeros son {Numeros_aleatorios}")
Media = mean(Numeros_aleatorios)
Mediana = median(Numeros_aleatorios)
Moda = mode(Numeros_aleatorios)
if Media > Mediana and Mediana > Moda:
    print(f"El sesgo es positivo, su media es de {Media}, su mediana es de {Mediana} y su moda de {Moda}")
elif Media < Mediana and Mediana < Moda:
    print(f"El sesgo es negativo, su media es de {Media}, su mediana es de {Mediana} y su moda de {Moda}")
else:
    print(f"No tiene sesgo, su media es de {Media}, su mediana es de {Mediana} y su moda de {Moda}")