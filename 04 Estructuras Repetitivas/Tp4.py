import random
print("Hola Mundo")
#Actividad 1
ContI = 0
for ContI in range (1,101):
    print(ContI, end=", ")
#Actividad 2
print("")
num = int(input("Ingrese un numero mayor de dos digitos preferiblemente: "))
n = abs(num) #el abs es por si ponen un numero negativo, lo convierte en positio
numC = 0
while n > 0:
    n = n // 10
    numC += 1
print(f"El nuemero {num} tiene una cantidad de {numC} digitos")
#Actividad 3
num = 0
num = int(input("Ingrese un numero para determinar el rango de la suma: "))
num1 = int(input("Ingrese un numero para determinar el final del rango de la suma: "))
if num < num1:
    lim1 = num + 1
    lim2 = num1 -1
    x = lim1
    resul = lim1
    for x in range(lim1, lim2, 1):
        x += 1
        resul += x
    print(f"la suma de los numeros dentro del rango es de {resul}")
elif num > num1:
    lim1 = num -1
    lim2 = num1 + 1
    x = lim1
    resul = lim1
    for x in range(lim1, lim2,-1):
        x -= 1
        resul += x
    print(f"la suma de los numeros dentro del rango es de {resul}")
else:
    print("No se puede realizar la suma de los numeros del rango determinado, ya que ambos son el mismo o no cumple con la condición necesaria")
#Actividad 4
resul = 0
Num = int(input("Ingrese un numero entero en la suma: "))
while Num != 0:
    resul = resul + Num
    Num = int(input("Ingrese un numero entero en la suma: "))
print(f"El resultado de la suma de los numeros ingresados es de {resul}")
#Actividad 5
print("Ahora debera de tratar de adininar el numero.")
intentos = 1
Num = random.randint(0,9)
num = int(input("Ingrese el numero:"))
while num != Num:
    intentos += 1
    num = int(input("Ingrese el numero:"))
print(f"Adivino el numero en {intentos} intentos")
#Actividad 6
ContI = 0
for ContI in range (100,-1,-2):
    print(ContI, end= ", ")
#Actividad 7
print("")
num = 0
num = int(input("Ingrese un numero para determinar el rango de la suma: "))
x = 0
resul = 0
for x in range(0, num, 1):
    x += 1
    resul += x
print(f"la suma de los numeros dentro del rango es de {resul}")
#Actividad 8
x =0
pos = 0
neg = 0
par = 0
impar = 0
for x in range(100):
    num = int(input("Ingrese el numero entero: "))
    if num > 0:
        pos = pos +1
    else:
        neg = neg +1
    if num % 2 == 0:
        par = par +1
    else:
        impar = impar +1
print(f"De los numeros escritos {pos} son positivos, {neg} son negativos, de esos {par} son pares y {impar} son impares")
#Actividad 9
numC = 100
x = 0
suma = 0
for x in range(numC):
    num = float(input("Ingrese el numero: "))
    suma = suma + num
Media = suma / numC
print(f"La media de los numero es de {Media}")
#Actividad 10
num = input("Ingrese  un numero")
Invert = ""
for dig in num:
    Invert = dig + Invert
print (f"Numero invertido es {Invert}")
#test