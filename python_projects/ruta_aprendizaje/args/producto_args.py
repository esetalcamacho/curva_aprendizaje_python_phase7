# Función que acepte un número variable de argumentos y devuelva el producto de todos ellos.

def producto(*numeros):
    resultado = 1 # Definimos la variable resultado como 1 para que se pueda ejecutar la aplicacion
    for numero in numeros:
        resultado *= numero
    print (resultado)

producto(2, 5, 8)
producto(3, 6, 5)
producto (9, 3)
