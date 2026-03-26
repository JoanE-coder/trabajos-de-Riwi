from modulo_servicios import agregar_producto, calcular_estadisticas, mostrar_inventario

inventario = []

while True:

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. calcular estadisticas")
    print("4. salir")

    opcion = input("SELECIONAR UNA OPCION: ")
    if opcion == "1":
        nombre = input("ingrese el nombre del poducto")

# Validamos que el precio sea un numero
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                break
            except:
                print("ERROR: ingrese un numero valido para el precio.")

    # validacion de la cantidad en número enteros
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                break
            except:
                print("ERROR: ingrese un numero valido para el precio.")

        agregar_producto(inventario, nombre, precio, cantidad)
        print("producto agregado correctamente.")

    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        calcular_estadisticas(inventario)
    elif opcion == "4":
        print ("Saliendo del programa")
        break
    else:
        print("Opcion invalida")