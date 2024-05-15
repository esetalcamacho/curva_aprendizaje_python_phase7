import re # Para expresiones regulares usamos la libreria re

frase = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar = "aprender"

textoEncontrado = re.search(textoBuscar, frase) # Nuevamente buscamos con el parametro de textoBuscar y luego en frase

print(textoEncontrado.start()) # El metodo start indica que la palabra incia en el espacio 8.
print(textoEncontrado.end()) # El metodo end indica que la palbra termina en el espacio 16.
print(textoEncontrado.span()) # El metodo span muestra en una tupla en que espacio de memoria esta.