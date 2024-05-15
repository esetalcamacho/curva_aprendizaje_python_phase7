# Acepta un número variable de argumentos de tipo string y devuelva una sola cadena que contenga la concatenación de todas las cadenas proporcionadas.

def frase(*palabras):
    concatenacion = ""
    for palabra in palabras:
        concatenacion += palabra
    print(concatenacion)

frase("Hola ","soy ", "Colombiano")
frase("Paz ", "y ", "amor")