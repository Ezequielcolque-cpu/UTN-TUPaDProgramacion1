#act 1
def factorial(n):
    """Calcula el factorial de un número de forma recursiva"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("="*50)
print("EJERCICIO 1: FACTORIAL")
print("="*50)
num = int(input("Ingrese un número entero positivo: "))
print(f"\nFactoriales desde 1 hasta {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


#act 2
def fibonacci(n):
    """Calcula el valor de Fibonacci en la posición n (recursivo)"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("\n" + "="*50)
print("EJERCICIO 2: FIBONACCI")
print("="*50)
posicion = int(input("¿Hasta qué posición desea ver la serie de Fibonacci? "))
print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")


#act 3
def potencia(base, exponente):
    """Calcula base^exponente de forma recursiva usando n^m = n * n^(m-1)"""
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
print("\n" + "="*50)
print("POTENCIA")
print("="*50)
base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
resultado = potencia(base, exp)
print(f"{base}^{exp} = {resultado}")

#act 4
def decimal_a_binario(n):
    """Convierte un número decimal a binario de forma recursiva"""
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)
print("\n" + "="*50)
print("EJERCICIO 4: DECIMAL A BINARIO")
print("="*50)
numero = int(input("Ingrese un número decimal para convertir a binario: "))
if numero == 0:
    binario = "0"
else:
    binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")

#act 5
def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo de forma recursiva"""
    # Caso base: si la palabra tiene 0 o 1 caracteres, es palíndromo
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
print("\n" + "="*50)
print("PALÍNDROMO")
print("="*50)
palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(palabra):
    print(f"'{palabra}' ES un palíndromo")
else:
    print(f"'{palabra}' NO es un palíndromo")


#act 6
def suma_digitos(n):
    """Calcula la suma de los dígitos de un número de forma recursiva"""
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)
print("\n" + "="*50)
print("SUMA DE DÍGITOS")
print("="*50)
numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

#act 7
def contar_bloques(n):
    """Calcula el total de bloques necesarios para una pirámide de n niveles"""
    if n == 0:
        return 0
    return n + contar_bloques(n - 1)
print("\n" + "="*50)
print("BLOQUES DE PIRÁMIDE")
print("="*50)
niveles = int(input("¿Cuántos bloques tiene el nivel más bajo de la pirámide? "))
total = contar_bloques(niveles)
print(f"Para una pirámide con {niveles} bloques en la base se necesitan {total} bloques en total")

#act 8
def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número"""
    if numero == 0:
        return 0
    coincide = 1 if (numero % 10) == digito else 0
    return coincide + contar_digito(numero // 10, digito)
print("\n" + "="*50)
print("CONTAR DÍGITO")
print("="*50)
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a buscar (0-9): "))

if 0 <= digito <= 9:
    apariciones = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {apariciones} veces en {numero}")
else:
    print("El dígito debe estar entre 0 y 9")
