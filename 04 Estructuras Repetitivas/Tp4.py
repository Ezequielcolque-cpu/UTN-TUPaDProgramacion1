print("Hola Mundo")
#Actividad 1
ContI = 0
for ContI in range (1,101):
    print(ContI)
#Actividad 2
num = int(input("Ingrese un numero mayor de dos digitos preferiblemente: "))
n = abs(num)
numC = 0
while n > 0:
    n = n // 10
    numC += 1
print(f"El nuemero {num} tiene una cantidad de {numC} digitos")