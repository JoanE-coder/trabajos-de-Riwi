# Inicio

hora = int(input("Que horario quiere agendar: "))

if hora >= 6 and hora <= 11:
    print("Esta agendado en hora de la mañana")

elif hora >= 12 and hora <= 17:
    print("Esta agendado en horas de la tarde")

elif hora >= 18 and hora <= 22:
    print("Esta agendado en horas de la noche")

else:
    print("Horario no disponible")        