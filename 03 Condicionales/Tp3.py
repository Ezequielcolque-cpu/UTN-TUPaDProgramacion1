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
#Actividad 7
Frase = input("Ahora ingrese una palabra o frase: ").lower()
if Frase.endswith(("a","e","i","o","u")):
    Frase= Frase + "!"
    print(Frase)
else:
    print(Frase)
#Actividad 8
Nombre = input("Ingrese su nombre: ")
print("A continuacion tendra que selecionar una de las 3 opciones, la primera pondrá su nombre en mayúsculas, la segunda pondrá su nomnbre en minúsculass y la tercera solo pondrá la primera letra en mayúscula")
Opcion = int(input("Ingrese la opcion (1/2/3)"))
if Opcion == 1:
    print(Nombre.upper())
elif Opcion == 2:
    print(Nombre.lower())
else:
    print(Nombre.capitalize())
#Actividad 9
print("Ahora me dirá una magnitud de un terremoto y yo se lo clasificaré")
Magnitud = float(input("Ingrese la magnitud del terremoto: "))
if Magnitud < 3:
    print("es un terremoto muy leve")
elif Magnitud < 4:
    print("es un terremoto leve")
elif Magnitud < 5:
    print("es un terremoto moderado")
elif Magnitud < 6:
    print("es un terremoto fuerte")
elif Magnitud < 7:
    print("es un terremoto muy fuerte")
else:
    print("es un terremoto extremo")
#Actividad 10
