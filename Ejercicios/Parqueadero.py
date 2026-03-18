# Inicio


cantidad = int(input("\n¿Cuantas horas duro?: \n"))

if cantidad == 1:
    total = 5000

else:
    total = 5000  +  (cantidad - 1) * 3000
    
    print(f"Total a pagar:", total)        

