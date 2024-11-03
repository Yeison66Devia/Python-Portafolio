def main():
    productos = {}
    while agregar_producto(productos):
        pass
    mostrar_productos(productos)
    calcular_total(productos)
