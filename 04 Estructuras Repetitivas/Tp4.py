print("Hola Mundo")
#Actividad 1
ContI = 0
for ContI in range (1,101):
    print(ContI)
#Actividad 2
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
#