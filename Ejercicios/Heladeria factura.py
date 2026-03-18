cono = 3000
vaso = 4000
banana_split = 9000

total = 0
clientes = 0
total_vendido = 0

cont_cono = 0
cont_vaso = 0
cont_banana = 0

continuar = "si"

while continuar == "si":

    print("\n === BIENVENIDO ===")
    print("\n Cono - Vaso - Banana split")
    sabor = input("\nQue saber de helado quiere: ").lower()
    cantidad = int(input("que cantidad desea: "))

    if sabor == "cono":
        total = cono * cantidad 
        cont_cono += cantidad

    elif sabor == "vaso":
        total = vaso * cantidad
        cont_vaso += cantidad

    elif sabor == "banana split":       
        total = banana_split * cantidad
        cont_banana += cantidad
        
    else:
        print("Ese sabor no exciste.")
        continuar
        
    total_vendido += total
    clientes += 1

    continuar = input("Desea continuar: (si/no)")

print("===Resumen===")
print("Total vendido:", total_vendido)
print("Clientes atendidos: ", clientes)

if cont_cono > cont_banana and cont_cono > cont_vaso:
    print("Producto mas vendido:", "Cono")    
elif cont_banana > cont_vaso:
    print("Producto mas vendido:", "Banana")
else:
    print("Producto mas vendido:", "Vaso")

