#Calculadora 
while True:

  def sumar(a,b):
    return a + b

  def restar(a,b):
    return a - b

  def dividir(a,b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

  def multiplicar(a,b):
    return a * b
 
  def potencia(a,b):
    return a ** b
 
  def raíz(a):
    if a < 0:
       return "Error: no se puede sar raíz de un numero negativo"
    return a ** 0.5
 
  def porcentaje(total,porc):
    return (total * porc)/100
 
  def promedio(a,b):
    return (a + b) / 2
  
  def modulo(a,b):
    if b == 0:
      return "ERROR: no se puede dividir entre cero"
    return a % b
  break

# MENÚ

while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Porcentaje")
    print("8. Promedio")
    print("9. Módulo")
    print("0. Salir")

    opcion = input("Elige una opción")

    if opcion == "0":
      print("Saliendo... Nos vemos...")
      break

    if opcion == "6": # Raíz solo necesita un número
      a = float(input("Ingresa el número:"))
      print("Resultado:", raíz(a))
    else:
      a = float(input("Ingresa el primer número:"))
      b = float(input("ingresa el segundo número"))

      if opcion == "1":
        print("Resultado:", sumar(a,b))

      elif opcion == "2":
        print("Resultado:", restar(a,b))    
        
      elif opcion == "3":
        print("Resultado:", multiplicar(a,b))

      elif opcion == "4":
        print("Resultado:", dividir(a,b))

      elif opcion == "5":
        print("Resultado:",potencia(a,b))

      elif opcion == "6":
        print("Resultado:", raíz(a,b))

      elif opcion == "7":
        print("Resultado:", porcentaje(a,b))

      elif opcion == "8":
        print("Resultado:", promedio(a,b))

      elif opcion == "9":
        print("Resultado:", modulo(a,b))

      else:
        print("Opción inválida")
          

