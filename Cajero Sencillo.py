# cajero automatico simple

# saldo inicial fijo
saldo= 1000
while True:

 operaciones = int(input("¿cuántas operaciones deseas realizar?"))

 for i in range(operaciones):
    print("\n---MENÚ---")
    print("1-- consultar saldo")
    print("2-- retirar dinero")
    print("3-- depositar dinero")

    opcion = input("seleccione una opción:")

    #opción 1: consultar saldo
    if opcion == "1":
        print(f"saldo actual: ${saldo}")
        
    #opción 2: retirar dinero
    elif opcion == "2":
        while True:
            monto = int(input("ingrese el monto a retirar: $"))

            if monto < 0:
                print("El monto no puede ser negativo. intente nuevamente")
            elif monto > saldo: 
                print("fondos insuficientes.")
                break
            else:
                saldo -= monto
                print(f"Retiro exitoso. nuevo saldo: ${saldo}")
    #submenú despues del retiro
            
                print("\n¿Qué deseas hacer ahora?")
                print("1--Consultar saldo")
                print("2--Volver al menú principal")
                print("3--Salir")

                sub_opcion = input("seleccione una opción")
                if sub_opcion == "1":
                    print(f"saldo actual: ${saldo}")
                    break
                elif sub_opcion == "2":
                    break #sale del submenu y vuelve al menú principal
                elif sub_opcion == "3":
                    print("Gracias por usar el cajero automático")
                    exit() #TERMINA COMPLETAMENTE EL PROGRAMA
                else:
                    print("Opción inválida") 
                    break   

    #opción 3: depositar dinero
    elif opcion == "3":
        while True:
            monto = float(input("ingrese el monto a depositar: $"))

            if monto < 0:
                print("El monto no puede ser negativo. Intente nuevamente.")
            else:
                saldo += monto
                print(f"Depósito exitoso. nuevo saldo: ${saldo}")
                break

    #opción invalida
    else:
        print("opción invalida")

     