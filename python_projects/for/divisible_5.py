number = int(input("Por favor inserte un numero: "))

if number % 5 == 0:
    if number >= 0:
        print(f"El {number} es positivo y divisible por 5")
    else:
        print(f"El {number} es negativo y divisible por 5")
else:
    if number >= 0:
        print(f"El {number} es positivo y no divisble por 5")
    else:
        print(f"El {number} es negativo y no divisible por 5")