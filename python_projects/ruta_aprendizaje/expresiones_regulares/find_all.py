import re

frase = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar = "Python"

print(re.findall(textoBuscar, frase)) # Nos devolvera en una lista las veces que se repite Python en la frase