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
 opcion = input( "SELECCIONE UNA OPCION:\n")

#OPCION 1: CLAVES
 if opcion == "1":
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
     
#OPCION 2: CONSULTAS DE MOVIMIENTO
 elif opcion == "2":
   if Movimiento:
     print("Movimientos recientes:")
     for mov in Movimiento:
       print(mov)
   else:
     print("No hay movimientos registrados.")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 3: PAGOS
 elif opcion == "3":
   print("Función de pagos no implementada aún.")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 4: RETIRO
 elif opcion == "4": 
   while True:
     try:
       Retirar_dinero = float(input("Ingrese el monto a retirar: $"))
       if Retirar_dinero < 0:
         print("El monto no puede ser negativo. Intente nuevamente.")
       elif Retirar_dinero > Saldo:
         print("Fondos insuficientes.")
         break
       else:
         Saldo -= Retirar_dinero
         Movimiento[f"Retiro: ${Retirar_dinero}"] = Saldo
         print(f"Retiro exitoso. Nuevo saldo: ${Saldo}")
         break
     except ValueError:
       print("Entrada inválida. Por favor, ingrese un número válido.")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 5: CONSULTAR SALDO
 elif opcion == "5":
   print(f"Saldo actual: ${Saldo}")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 6: TRANSFERENCIA
 elif opcion == "6":
   print("Función de transferencia no implementada aún.")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 7: DEPOSITAR
 elif opcion == "7":
   while True:
     try:
       Deposito = float(input("Ingrese el monto a depositar: $"))
       if Deposito < 0:
         print("El monto no puede ser negativo. Intente nuevamente.")
       else:
         Saldo += Deposito
         Movimiento[f"Depósito: ${Deposito}"] = Saldo
         print(f"Depósito exitoso. Nuevo saldo: ${Saldo}")
         break
     except ValueError:
       print("Entrada inválida. Por favor, ingrese un número válido.")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break
 else:
   print("Opción inválida. Por favor, seleccione una opción válida.")