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

def mostrar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    print("\nProductos y precios:")
    print("{:<20} {:<10}".format("Producto", "Precio"))
    print("-" * 30)
    for nombre, precio in productos.items():
        print("{:<20} ${:<10.2f}".format(nombre, precio))

def calcular_total(productos):
    total_general = 0
    print("\nIngrese la cantidad para cada producto:")
    for nombre, precio in productos.items():
        cantidad = solicitar_cantidad(nombre)
        total_producto = precio * cantidad
        total_general += total_producto
        print(f"Total para {nombre}: ${total_producto:.2f}")
    print(f"\nTotal general: ${total_general:.2f}")

def solicitar_cantidad(nombre):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad para {nombre}: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
            return cantidad
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def main():
    productos = {}
    while agregar_producto(productos):
        pass
    mostrar_productos(productos)
    calcular_total(productos)

if __name__ == "__main__":
    main()
