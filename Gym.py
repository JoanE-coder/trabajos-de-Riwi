# Inicio

edad = int(input("\nIngrese su edad: \n"))

if edad < 13:
    print("No esta permitido menores")

elif edad >= 13 and edad <= 17:
    print("Estas en la clase Juvenil")

elif edad >=18 and edad <= 59:
    print("Estas en la clase General")

else:
    print("Estas en la clase senior")        