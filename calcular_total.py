def calcular_total(productos):
    total_general = 0
    print("\nIngrese la cantidad para cada producto:")
    for nombre, precio in productos.items():
        cantidad = solicitar_cantidad(nombre)
        total_producto = precio * cantidad
        total_general += total_producto
        print(f"Total para {nombre}: ${total_producto:.2f}")
    print(f"\nTotal general: ${total_general:.2f}")
