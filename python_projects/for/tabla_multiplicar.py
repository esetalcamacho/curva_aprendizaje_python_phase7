numero = int(input("Por favor, ingresa un número para saber su tabla de multiplicar: "))

for element in range (1,11):
    resultado = numero * element
    print(f"{numero} * {element} = {resultado}")