from funciones import agregar_producto, mostrar_productos, calcular_total

def main():
    productos = {}
    
    while True:
        if not agregar_producto(productos):
            break
            
    mostrar_productos(productos)
    calcular_total(productos)

if __name__ == "__main__":
    main()
