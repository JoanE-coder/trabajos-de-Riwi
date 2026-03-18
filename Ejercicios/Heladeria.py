# Variables para el resultado

vainilla = 0
chocolate = 0
fresa = 0

# Inicio de chiclo
print("     ""\n==== BIENVENIDO ====\n")
for i in range (5):
    sabor = input("Ingrese el sabor del Helado: \n").lower()
    
    if sabor == "vainilla":
       vainilla += 1

    elif sabor == "chocolate":
        chocolate += 1

    elif sabor == "fresa":
        fresa += 1 

    else:
        print(" Error: ingrese algun sabor de la lista")  

# Resumen de los pedidos

print("\n=== Resumen De Pedidos ===\n")
print("Vainilla: ", vainilla)
print("Chocolate: ", chocolate)  
print("Fresa: ", fresa)    