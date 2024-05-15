# Escribe una función que acepte un número variable de argumentos y devuelva el valor máximo entre todos ellos.

def mayor(*numeros):
    return max(numeros)

print(mayor(5, 2, 8, 10, 3))