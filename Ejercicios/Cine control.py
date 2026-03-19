# Inicio

total_personas = 0
niños = 0
adultos = 0
ancianos = 0

capacidad = int(input("- Ingrese la capacidad del cine: "))

for i in range(capacidad):
    print(f"\npersona #{i + 1}")
    edad = int(input("- Ingrese la edad: "))
    total_personas += 1

    if edad < 18:
        niños += 1

    elif edad < 60:
        adultos += 1

    else:
        ancianos += 1 

    continuar = input("- ¿Desea ingresar otra persona? (s/n): ").lower() 
    if continuar != "s":
        break

print("\n--- Resumen ---")
print(f"Total de personas: {total_personas}")
print(f"Niños: {niños}")
print(f"Adultos: {adultos}")
print(f"Ancianos: {ancianos}")

if total_personas == capacidad:
    print("La sala se lleno")
else:
    print("La sala no se lleno")    