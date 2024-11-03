def mostrar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    print("\nProductos y precios:")
    print("{:<20} {:<10}".format("Producto", "Precio"))
    print("-" * 30)
    for nombre, precio in productos.items():
        print("{:<20} ${:<10.2f}".format(nombre, precio))