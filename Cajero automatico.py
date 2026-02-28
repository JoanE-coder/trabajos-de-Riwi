Salir = False
Saldo = 0
Retirar_dinero = 0
Movimiento = {}
Deposito = 0
Clave = 123456

while not Salir:

 print("       ""SELECCIONE SU OPERACION"" \n ")
 print("GESTION DE RETIRO RAPIDO \n")
 print("1. CLAVES             2. CONSULTAS DE MOVIMIENTO \n")
 print("3. PAGOS              4. RETIRO\n")
 print("5. CONSULTAR          6. TRANSFERENCIA\n")
 print("7. DEPOSITAR\n") 
 opcion = input( "SELECCIONE UNA OPCION:")

 if opcion == "1":
  print ("1. Ver clave")
  
  opcion = int(input("Seleccione una opcion\n"))
  if opcion == 1:
    print (f"Tus claves son: {Clave}\n")
    while True:

     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break

  if opcion == "2":
    print ("Estos son tus movimientos")
    
    Deposito = float(input("Ingrese monto a depositar"))
    Saldo += Deposito
    Movimiento.append(f"depósito: ${Deposito}")

    retiro = float(input("Ingrese monto a retirar"))

    if retiro <= Saldo:
      Saldo -= retiro
      Movimiento.append(f"Retiro: ${retiro}")
    else:
      print("fondos insuficiente")

      print("\n--- Historial de movimientos---")
      for movimiento in movimiento:
        print(movimiento)
        



