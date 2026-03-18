# Inicio
cantidad = 0

for i in range(6):
 
 nombre = input("Digite nombre de estudiante: ")
 
 asistencia = int(input("Ingrese numero e Asistencias: "))

 if asistencia < 5:
    print("Asistencia Baja")

 elif asistencia >= 5 and asistencia <= 8:
    print("Asistencia Media")    
    
 else:
    print("Asistencia Alta") 

