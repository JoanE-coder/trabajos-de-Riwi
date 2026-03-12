# Variables

cafe = 4000
té = 3500
jugo = 5000

# Menú

bebida = input("¿Que bebida desea? (cafe, te, jugo): ").lower()
cantidad = int(input("¿Que cantidad desea?: "))

# Calculo

if bebida == "cafe":
     total = cafe * cantidad
elif bebida == "te":
    total = té * cantidad 
elif bebida == "jugo":
    total = jugo * cantidad
else:
    print("Bebida no disponible")
    total = 0
# Resultado

if total > 0:
    print("total a pagar: ", total)    

