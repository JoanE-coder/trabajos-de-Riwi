# Inicio 

print("   ""\n=== Binevenido ===")
print("  ""\nPerro - Gato - Conejo")
mascota = input("\nQue mascota tiene:").lower()

if mascota == "perro":
    print("Le Recomendamos: Para Cachorro, Dog Chow - Para adultos, Max Senior")

elif mascota == "gato":
    print("Le Recomendamos: Mirringo - Cat Chow")

elif mascota == "conejo":
    print("Le Recomendamos: Verduras como zanahoria o brócoli")

else:
    print("No tenemos para esas mascotas")  