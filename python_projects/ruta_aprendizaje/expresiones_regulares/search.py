import re

frase = "Vamos a aprender de expresiones regulares"

# print(re.search("aprender", frase)) # Usamos el metodo search para encontrar la palabra y la variable donde esta

textoBuscar = "Vamos"

if re.search(textoBuscar, frase) is not None: # Usamos la variable textoBuscar como el parametro de busqueda y frase el lugar a buscar.
    print("He encontrado el texto") # Este if nos permite simplificar el mensaje que muestra de objeto encontrado.
else:
    print("No he encontrado el texto")


