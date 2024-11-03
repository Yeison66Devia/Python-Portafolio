def calcular_total(productos):
    total_general = 0
    print("\nIngrese la cantidad para cada producto:")
    for nombre, precio in productos.items():
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad para {nombre}: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa. Intente de nuevo.")
                    continue
                total_producto = precio * cantidad
                total_general += total_producto
                print(f"Total para {nombre}: ${total_producto:.2f}")
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
    print(f"\nTotal general: ${total_general:.2f}")