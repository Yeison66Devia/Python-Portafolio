def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        return False
    try:
        precio = float(input("Ingrese el precio unitario del producto: "))
        productos[nombre.upper()] = precio
    except ValueError:
        print("Error: Debe ingresar un precio válido.")
    return True
