# Codigo de la caja de una tienda
import time # Para medir el tiempo y ejecucion de mi codigo
import datetime # Para manejar la hora y fecha

def fecha_hora_compra():
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y %H:%M")
    return fecha_hora_formateada

def datos_cliente():
    cliente = {}
    nombre = input("Ingrese su nombre:")
    while True:
        try:
            identificacion = int(input("Ingrese su numero de identificación"))
            break # Fin del bucle si todo esta ok
        except ValueError:
            print("Ingrese solo números sin puntos ni comas")
    # Se almacenan el nombre y el número de identificación en el diccionario cliente.
    cliente['nombre'] = nombre
    cliente['identificacion'] = identificacion

    return cliente

def obtener_producto(productos):
    while True: # Mientras sea verdadero se ejecuta este bloque, y termina si escribimos fin.
        producto = input("Ingrese un producto (o escriba 'fin' para terminar): \n").lower()
        if producto == "fin": # Termina el algoritmo
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
        producto = obtener_producto(productos) # Permite seleccionar productos de la lista
        if producto is None: # Si no se selecciona productos se cancela
            if not compra:
                return
            break

        precio = productos[producto] # Se obtiene el precio del producto en el diccionario
        print(f"Producto: {producto.capitalize()}, Precio: ${precio} \n") # Imprime los detalles del producto

        cantidad = obtener_cantidad() # Llamamos a la funcion obtener cantidad

        impuesto = impuestos.get(producto, 0) # Se obtiene el impuesto asociado en el diccionario.
        precio_total_producto, precio_total_con_impuesto_producto = calcular_precio_con_impuesto(precio, impuesto, cantidad) # Llamamos la funcion calcular precio con impuesto
        precio_total += precio_total_producto
        precio_total_con_impuesto += precio_total_con_impuesto_producto

        if producto in compra: # Si el producto ya está en el registro de compra, se actualiza la cantidad y los precios totales.
            compra[producto]['cantidad'] += cantidad
            compra[producto]['precio_total'] += precio_total_producto
            compra[producto]['precio_total_con_impuesto'] += precio_total_con_impuesto_producto
        else: # Si el producto no está en el registro de compra, se agrega con su cantidad y precios totales.
            compra[producto] = {
                'cantidad': cantidad,
                'precio_total': precio_total_producto,
                'precio_total_con_impuesto': precio_total_con_impuesto_producto
            }

        agregar = input("¿Deseas agregar otro producto 1.Si / 2.No: ")
        if agregar != "1":  # Si el usuario no ingresa "1", el bucle se rompe.
            break
        print("¡Producto agregado con éxito \n")
    # Muestra los datos almacenados en mi compra
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

# Inicializamos las funciones
comprando(productos, impuestos)

# Tiempos de ejecución

# Funcion Cliente

start_time = time.time() # Captura tiempo antes de la ejecucion
cliente = datos_cliente()
end_time = time.time() # Captura tiempo despues de la ejecucion
print(f"Tiempo de ejecucucion de la funcion datos_cliente: {end_time-start_time:.2f} segundos")

# Funcion comprando

start_time = time.time()
compra, precio_total, precio_total_con_impuesto, fecha_hora_compra = comprando(productos, impuestos)
end_time = time.time()
print(f"Tiempo de ejecución de comprando: {end_time - start_time:.2f} segundos")
