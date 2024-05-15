def comprando(**productos):
    compra = {}  # Diccionario donde se almacenará mi compra
    precio_total = 0  # Inicializamos el precio total sin impuestos
    precio_total_con_impuesto = 0  # Inicializamos el precio total con impuesto

    while True:
        producto = input("Ingrese un producto (o escriba 'fin' para terminar): \n").lower() 
        if producto == 'fin':
            if not compra: # En caso de que se escriba fin se dirije al return
                return
            break
        precio = productos.get(producto)
        if precio is None:
            print("¡Producto no encontrado!")
            continue
        print(f"Producto: {producto.capitalize()}, Precio: ${precio} \n")

        while True: # Si por error ingresa texto en lugar de numeros, el software informa el error y reiniciar nuevamente el proceso.
            try: 
                cantidad = int(input("Ingrese la cantidad del producto: \n"))
                break
            except ValueError:
                print("Cantidad Invalida. Por favor, ingrese un numero entero")

        precio_total += precio * cantidad
        impuesto = float(impuestos.get(producto, 0))
        precio_con_impuesto = precio * (1 + impuesto)
        precio_total_con_impuesto += precio_con_impuesto * cantidad

        if producto in compra:
            compra[producto]['cantidad'] += cantidad
            compra[producto]['precio_total'] += precio * cantidad
            compra[producto]['precio_total_con_impuesto'] += precio_con_impuesto * cantidad
        else:
            compra[producto] = {
                'cantidad': cantidad,
                'precio_total': precio * cantidad,
                'precio_total_con_impuesto': precio_con_impuesto * cantidad
            }

        agregar = input("¿Deseas agregar otro producto? 1.Si / 2.No: ")
        if agregar != '1':
            break
        print("¡Producto agregado con éxito! \n")

    print("\nLista de productos comprados:")

    for producto, detalles in compra.items():
        print(f"{producto.capitalize()}: Cantidad: {detalles['cantidad']}, Precio Total: ${detalles['precio_total']:.2f}, Precio Total con Impuesto: ${detalles['precio_total_con_impuesto']:.2f}")

    print(f"\nPrecio Total sin Impuestos: ${precio_total:.2f}")
    print(f"Precio Total con Impuestos: ${precio_total_con_impuesto:.2f}")

productos = {
    "arroz": 3000,
    "atun": 2000,
    "frijol": 1500,
    "salchichas": 2400
}

impuestos = {
    "arroz": 0.2,  # Impuesto del 20%
    "atun": 0.1,  # Impuesto del 10%
    "frijol": 0.06,  # Impuesto del 6%
    "salchichas": 0.2  # Impuesto del 20%
}

comprando(**productos)