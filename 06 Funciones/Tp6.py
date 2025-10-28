#print("Hello Wordl")

def imprimir_hola_mundo():
    return "Hello Wordl"

def Saludo_usuario(nom):
    return f"Hola {nom}, como te va?"

def info_personal(nom,apell,edad,resid):
    return f"Hola {nom} {apell}, de {edad} años de {resid}"

#main program
print(imprimir_hola_mundo())
nom = input("ingrese un nombre ")
print(Saludo_usuario(nom))
nom = input("ingrese un nombre ")
apell = input("ingrese un apellido ")
edad =int(input("Ingrese ssu edad "))
resid = input("ingrese un residencia ")
print(info_personal(nom, apell, edad, resid))