

cafe = 4000
capuchino = 7000
pastel = 6000
total = 0

print("\n === BIENVENIDO ===")
print("\n Café - Capuchino - pastel")

bebidas = input("\n- Que bebida desea: ").lower()
cantidad = int(input("\n- Que cantidad desea: "))

if bebidas == "cafe":
    total = cafe * cantidad

elif bebidas == "capuchino":
    total = capuchino * cantidad 

elif bebidas == "pastel":
    total = pastel * cantidad

else:
    print("- No exite -")
    total = 0

if total > 20000:
    descuento = total * 0.10
    total_final = total - descuento
    
    print("\n- Subtotal: ", total)
    print("\n- Descuento: ", descuento)
    print("\n- Total a pagar: ", total_final)

else:
    print("\n-Total a pagar: ". total)        