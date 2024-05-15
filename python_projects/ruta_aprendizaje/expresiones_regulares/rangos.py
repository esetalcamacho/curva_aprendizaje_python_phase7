import re

nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana"]

for elemento in nombres:
    if re.findall("^[O-T]", elemento): # Especificamos que queremos los nombres que estan entre O y T
        print(elemento)

ciudades = ["Bog1", "Med1", "Bog2", "Cal1", "Bog3", "Cal2", "BogC", "BogP", "MedO"]
for ciudad in ciudades:
    if re.findall("Bog[1-3A-Z]", ciudad): # Podemos usar los terminos que queramos desde letras y numeros
        print(ciudad)