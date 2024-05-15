# Funcion que acepte un numero variable de argumentos de palabras clave imprimir cada clave y su valor asociado

def palabras(**clave):
    for clave, valor in clave.items():
        print(f"{clave}:{valor}")

palabras(Auto = "Volkswagen", Modelo = "Jetta", Año="2022")