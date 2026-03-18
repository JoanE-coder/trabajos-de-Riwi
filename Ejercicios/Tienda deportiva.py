# Inicio

productos = 0

for i in range (6):

 precio = int(input("Ingrese precio de los proguctos: "))

 if precio > 100000:
    productos += 1


print("Productos mayores de 100k: ", productos)