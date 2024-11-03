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
