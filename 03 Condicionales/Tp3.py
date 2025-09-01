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