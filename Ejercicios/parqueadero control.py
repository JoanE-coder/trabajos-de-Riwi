# Inicio

carro = 4000
moto = 2000

contador_carros = 0
contador_motos = 0

for i in range(2):
    tipo_vehiculo = input("Ingrese el tipo de vehículo (carro/moto): ").lower()
    horas_estacionado = int(input("Ingrese las horas estacionado: "))

    if tipo_vehiculo == "carro":
        tarifa = carro
        contador_carros += 1
    elif tipo_vehiculo == "moto":
        tarifa = moto
        contador_motos += 1
    else:
        print("Tipo de vehículo no válido.")
        continue

    total_pagar = tarifa * horas_estacionado
    print(f"Total a pagar: {tipo_vehiculo}: {total_pagar}")

print(" === resumen ===")
print("Carros ingresados: ", contador_carros)    
print("Motosingresados: ", contador_motos)
