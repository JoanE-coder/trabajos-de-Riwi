# Inicio

nombres = []
bajo = 0
medio = 0
alto = 0


print(" === BIENVENIDO === ")
for i in range(3):
 
    nombre = input("\n- Ingresar Nombre: ")
    dia = int(input("\n- Ingrese los dias:"))

    if dia < 3:
       print("- Bajo Compromiso")
       bajo += 1

    elif 3 <= dia <= 4:
        print("- Compromiso Medio")
        medio += 1

    else:
        print("- Compromiso Alto")    
        alto += 1

print("\n === Resumen ===") 
print("Categoria Bajo: ", bajo )
print("Categoria Medio: ", medio)
print("Categoria Alto: ",alto)