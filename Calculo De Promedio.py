# Reglas

DESARROLLO_DE_SOFTWARE = 0.60 
HABILIDADES_SOCIOEMOCIONALES = 0.20
INGLES = 0.20

# Variables para los resumen

total_coders = 0
suma_promedios = 0

Reprobados = 0
Regulares = 0
Excelentes = 0

Mejor_Promedio = -1
Mejor_Coder = ""

# Entrada De Modulo

modulo = input("Ingresar Nombre Del Modulo: ")

continuar = True

while continuar:

    print("\n === Registro de coder ===")
    nombre = input("Nombre del coder")

# Validación de notas 

while True:
    desarrollo = float(input("Nota Desarrollo de software (0-100): "))
    if 0 <= desarrollo <=100:
        break
    else:
        print("ERROR: La nota debe estar entre 0 y 100")

while True:
    socio = float(input("Nota de Habilidades Socioemocionales (0-100):"))
    if 0 <= socio <= 100:
        break
    else:
        print("ERROR: La nota debe estar entre 0 y 100")        

while True:
    ingles = float(input("Nota de Inglés (0-100): "))
    if 0 <= ingles <= 100:
        break
    else:
        print("ERROR: La nota debe estar entre 0 y 100")
        
# Calculo de promedio
promedio =(
    desarrollo * DESARROLLO_DE_SOFTWARE +
    socio * HABILIDADES_SOCIOEMOCIONALES +
    ingles * INGLES )   

# Clasificacion
if promedio <=49:
    clasificacion = "Reprobado"
    Reprobados += 1
elif promedio <= 79:
    clasificacion = "Regular"
    Regulares += 1    
    
        