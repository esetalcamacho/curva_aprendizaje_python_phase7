import re

lista_nombres = ["Ana Gomez",
                 "Maria Martin",
                 "Sandra López",
                 "Santiago Martin",
                 "Sandra Perez"]

for elemento in lista_nombres: # Declaramos un elemento para buscarlo en listas con el ciclo for
    if re.findall("^Sandra", elemento): #Usamos el elemento sandra para buscar
        print(elemento) # Nos imprime el valor completo en este caso Sandra lopez

for elemento in lista_nombres: # Declaramos un elemento para buscarlo en listas con el ciclo for
    if re.findall("Martin$", elemento): #Usamos el elemento Martin para buscar
        print(elemento) # Nos imprime el valor completo en este caso las personsa que se apellidan martin

animales = ["perro", "gato", "pájaro", "elefante", "león", "ñandú"]

for animal in animales:
    if re.findall("[ñ]", animal): # En este caso solicitamos que nos muestre lso animales que tienen una ñ
        print(animal)

acentos = ["arbol", "pera", "helipuerto", "árbol", "banana", "cartagena"]

for acento in acentos:
    if re.findall("[aá]rbol", acento): # Imprimimos las palabras que tengan tilde o no la tengan, ideal para limpiar listas
        print(acento)
