import re

nombre1 = "Sandra López"
nombre2 = "Maria López"
nombre3 = "sandra Gómez"

if re.match("Sandra", nombre3, re.IGNORECASE): #Aqui decimos que omita las mayusculas y minusculas
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos enconrtado")

cadena1 = "Jara Lopez"
cadena2 = "5678925"
cadena3 = "a569878"

if re.match("\d", cadena3): # Buscamos un digita en la cadena dos
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado el número")