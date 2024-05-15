import re

nombre1 = "Jara López"
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"

if re.search("Lopez", nombre3, re.IGNORECASE): #Aqui decimos que omita las mayusculas y minusculas
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")