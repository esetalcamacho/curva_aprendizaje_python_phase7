def saludar(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Ejemplo de llamada a la función con diferentes argumentos de palabras clave
saludar(nombre="Juan", edad=30, ciudad="Madrid")
