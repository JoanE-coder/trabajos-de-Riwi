def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

def mostrar_inventario(inventario):
    #Verificamos si la lista esta vacia
    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        print("=== INVENTARIO ===")
        # Recorremos la lista con un for
        for producto in inventario:
            print(f"producto:{producto['nombre']} | Precio:{producto['precio']} | Cantidad: {producto['cantidad']}")
            print()
  
def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("No hay productos para calcular estadisticas")
        return
    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print("\n --- ESTADISTICAS --- ")
    print(f"valor total de inventario: {valor_total}")
    print(f"Cantidad total de producto: {total_productos}\n")