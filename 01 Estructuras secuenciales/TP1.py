#actividad 1
print("Hola mundo")
#actividad 2
print("¿Como te lamas?")
nombre =input ("Ecribe tu nombre: ")
nombre = str(nombre)
print(f"Hola {nombre}, un gusto en conocerte")
#actividad 3
print("Me Gustaría conocerte mejor, me dices cual es tu nombre, apellido y edad?")
nombre =input ("Ecribe tu nombre: ")
nombre = str(nombre)
apellido =input ("Ecribe tu apellido: ")
apellido = str(apellido)
edad =input ("Ecribe tu edad: ")
edad = int(edad)
print(f"Entonces tu nombre completo es {nombre} {apellido} de {edad} años, es bueno saberlo")
#actividad 4
print(f"Ok, ahora vamo a calcular el area y perimetro de un circulo, {nombre} serías tan amable de decirme el radio del circulo, solo dime el numero despues le asignamos una medida")
radio = int(input ("Ecribe el radio: "))
medida = str(input("Escirbe el tipo de medida:"))
pi= 3.14159
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"Bueno, ya he calculado el area del circulo es de {area}{medida} y el perimetro es de {perimetro}{medida}")
#actividad 5
print("Sigamos experimentando, ahora vamos a intertar con el tiempo.")
print("Me vas a decir una cantidad de segundos y yo te lo dire en horas")
segundos = int(input("Ingrese los segundos:"))
hora = segundos // 3600
print(f"Ya he calculado los {segundos} segundos en la/s hora/s y es {hora} hora/s")
#actividad 6
print("Ahora dime un numero y yo te dire su tabla de multiplicacion")
numero = int(input("Escribe el numero:"))
multiplo =  1
while multiplo!= 11:
    resultado = numero * multiplo
    print(f"{numero}*{multiplo}={resultado}")
    multiplo += 1
#actividad 7
print(f"Sigamos con algo simple {nombre}")
print("Ahora te pedire 2 numeros y te mostrare su suma,resta, division y multiplicasion")
numero = int(input("Esscribe el primer numero:"))
numero2 = int(input("Esscribe el segundo numero:"))
suma = numero + numero2
resta = numero - numero2
division = numero / numero2
multiplicacion = numero * numero2
mate = [suma, resta, division, multiplicacion]
print(f"Ahora te motrare los ressultados en el orden anteriormen dicho, {mate}")
#actividad 8
print("Continuemoss con el IMC (indice de masa corporal) ahora te pedire tus datos y te dire tu IMC")
altura = float(input("Escribe tu altura:"))
peso = float(input("Ahora tu peso:"))
IMC = peso / altura ** 2
print(f"Tu IMC es de {IMC}")
#actividad 9
print("Prosigamo con algo un poco más complicado, ahora transformare la temperatura de celcius a fahrenheit")
grados = float(input("Ingrese los grados celcius:"))
fahrenheit = grados * 1.8 + 32
print(f"Los {grados} grados en celcius son {fahrenheit} en fahrenheit")
# actividad 10
print("Y para terminar, hagamo algo simple, dame 3 numeros y te dire su promedio")
numero = int(input("Esscribe el primer numero:"))
numero2 = int(input("Esscribe el segundo numero:"))
numero3 = int(input("Esscribe el tercer numero:"))
promedio = (numero + numero2 + numero3) / 3
print(f"El promedio de los numeros dados es de {promedio} en total")