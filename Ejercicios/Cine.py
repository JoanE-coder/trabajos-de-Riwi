edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Niño, Paga $8000")
elif 12 <= edad <= 59:
   print("Adulto, Paga $12000")
else:
    print("Mayores, paga: $9000")        