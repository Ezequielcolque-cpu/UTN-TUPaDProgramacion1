print ("Hola")
#Activida 1 y 4
Edad = int (input ("Me podrías decir tu edad por favos"))
if Edad < 12:
    print (f"Usted es un niñ@ de {Edad}")
elif Edad < 18:
    print(f"Usted es un adolecente de {Edad}")
elif Edad < 30:
    print(f"Usted es mayor de edad, un adult@ joven de {Edad}")
elif Edad < 60:
    print(f"Usted es un adult@ de {Edad}")
else :
    print(f"Usted es una persona mayor/abuel@ de {Edad}")