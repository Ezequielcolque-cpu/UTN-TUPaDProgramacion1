#print("Hello Wordl")

def imprimir_hola_mundo():
    return "Hello Wordl"

def Saludo_usuario(nom):
    return f"Hola {nom}, como te va?"

#main program
print(imprimir_hola_mundo())
nom = input("ingrese un nombre ")
print(Saludo_usuario(nom))