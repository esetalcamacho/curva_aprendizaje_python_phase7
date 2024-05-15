"""
Escribe un programa que solicite al usuario una palabra y luego cuente cuántas veces aparece cada letra en esa palabra.
"""

def contarCaracteres(palabra):
    caracteres = {}
    for letra in palabra.lower():
        if letra != " ":
            if letra in caracteres:
                caracteres[letra] += 1
            else:
                caracteres[letra] = 1
    return caracteres

palabra = input("Ingresa una palabra: \n") # Definimos la palabra a ingresar
caracteres = contarCaracteres(palabra) # Ejecutamos la funcion

print("La cantidad de letras en esta palabra es:")
for letra, count in contarCaracteres(palabra).items():
    print(f"{letra}: {count}")