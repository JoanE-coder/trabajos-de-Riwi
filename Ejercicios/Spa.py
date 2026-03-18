# Inicio

print("   ""\n=== Binevenido ===")
print("  ""\nMasaje - Facial - Manicure\n")
servicios = input("* Que servicios desea: ").lower()

if servicios == "masaje":
    print("\n- Espere su llamada para su servicio de Masaje")

elif servicios == "facial":
    print("\n- Espere su llamada para su servicio de Facial")

elif servicios == "manicure":
    print("\n- Espere su llamada para su servicio de Manicure")

else:
    print("\n- Lo sentimos no aplicamos esos servicios")        