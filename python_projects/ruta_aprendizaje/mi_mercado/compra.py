# Codigo de la caja de una tienda

def obtener_producto(productos):
    while True: # Mientras sea verdadero se ejecuta este bloque, y termina si escribimos fin.
        producto = input("Ingrese un producto (o escriba 'fin' para terminar): \n").lower()
        if producto == "fin": # TErmina el algoritmo
            return None
        if producto in productos: # Busca el producto en el diccionario productos
            return producto
        else:
            print("Producto no encontrado")

def obtener_cantidad():
    while True:
        try: # Aqui condicionamos a que el usuario coloque la cantidad correcta
            cantidad = int(input("Ingrese la cantidad del producto: \n"))
            return cantidad
        except ValueError:
            print("Cantidad invalida. Por favor ingrese un numero entero." )

def calcular_precio_con_impuesto(precio, impuesto, cantidad):
    precio_total = precio * cantidad
    precio_con_impuesto = precio * (1 + impuesto) * cantidad
    return precio_total, precio_con_impuesto

def mostrar_compra(compra):
    print("\nLista de productos comprados:")
    for producto, detalles in compra.items():
        print(f"{producto.capitalize()}: Cantidad: {detalles['cantidad']}, Precio Total: ${detalles['precio_total_con_impuesto']:.2f}")

def comprando(productos, impuestos): # Atributos necesarios para el calculo
    compra = {} # Diccionario donde se almacenaran los itens de compra
    precio_total = 0 # Iniciamos la cuenta en 0
    precio_total_con_impuesto = 0 # Iniciamos la cuenta en 0

    while True:
        producto = obtener_producto(productos) # Pedir explicacion
        if producto is None:
            if not compra:
                return
            break

        precio = productos[producto]
        print(f"Producto: {producto.capitalize()}, Precio: ${precio} \n") # Imprime los detalles del producto

        cantidad = obtener_cantidad()

        impuesto = impuestos.get(producto, 0)
        precio_total_producto, precio_total_con_impuesto_producto = calcular_precio_con_impuesto(precio, impuesto, cantidad)
        #Explicar
        precio_total += precio_total_producto
        precio_total_con_impuesto += precio_total_con_impuesto_producto
        #Explicar
        if producto in compra:
            compra[producto]['cantidad'] += cantidad
            compra[producto]['precio_total'] += precio_total_producto
            compra[producto]['precio_total_con_impuesto'] += precio_total_con_impuesto_producto
        else:
            compra[producto] = {
                'cantidad': cantidad,
                'precio_total': precio_total_producto,
                'precio_total_con_impuesto': precio_total_con_impuesto_producto
            }

        agregar = input("¿Deseas agregar otro producto 1.Si / 2.No: ")
        if agregar != "1":
            break
        print("¡Producto agregado con éxito \n")
    #Explicar
    mostrar_compra(compra)

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

#Explicar creo que es porque esta iniciando la funcion
comprando(productos, impuestos)
