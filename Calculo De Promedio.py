# Reglas

DESARROLLO_DE_SOFTWARE = 0.60 
HABILIDADES_SOCIOEMOCIONALES = 0.20
INGLES = 0.20
modulo_valido = {"desarrollo", "socioemocionales", "ingles"}

# Variables para los resumen

total_coders = 0
suma_promedios = 0

Reprobados = 0
Regulares = 0
Excelentes = 0

Mejor_Promedio = -1
Mejor_Coder = ""

# Entrada De Modulo
while True:
 
  modulo = input("Ingresar Nombre Del Modulo: \n").lower() 
  if modulo in modulo_valido:
    break
  else:
    print("\nERROR: Modulo no valido. intente nuevamente.\n")

continuar = True

while continuar:

    print("=== Registro de coder ===\n")
    nombre = input("Nombre del coder: ")

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

    else:
        clasificacion = "Excelente"
        Excelentes +=1      
        
    # Alerta 
    alerta = ""
    if desarrollo < 50:
        alerta = "Debe reforzar el frente tecnico principal"

    # Resultados del coder

    print("=== RESULTADO ===\n")
    print("Modulo:", modulo)
    print("Coder:", nombre)
    print("Promedio Final: ", round(promedio, 2))
    print("Clasificación:", clasificacion)

    if alerta != "":
        print(alerta)

# Actualizar Resumen

    total_coders += 1
    suma_promedios += promedio

# Mejor coder
    if promedio > Mejor_Promedio:
        Mejor_Promedio = promedio
        Mejor_Coder = nombre

# Continuar o Salir

    opcion = input("¿Desea registrar otro coder? (S/N)\n")

    if opcion.lower() != "s":
        continuar = False

# Resumen Final

if total_coders > 0:
    promedio_general = suma_promedios / total_coders

else:
    promedio_general = 0

print("===== Resumen Del Modulo =====\n")
print("Modulo:", modulo)
print("Total De Coders:", total_coders)
print("Promedio General:", round(promedio_general, 2))
print("Reprobados:", Reprobados)
print("Regular:", Regulares)
print("Exelentes:", Excelentes)

if Mejor_Coder != "":
    print("Mejor Coder:", Mejor_Coder, "Con Promedio", round(Mejor_Promedio, 2))
        