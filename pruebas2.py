import time, datetime, os
total_seconds = 5
i = 0
while total_seconds > 0:
    timer = datetime.timedelta(seconds = total_seconds) #Variable que va disminuyendo Temporizador
    crono = datetime.timedelta(seconds = i) #Variable que va aumentando Cronometro
    print("Tiempo restante de proceso: ", timer, "\tTiempo transcurrido de proceso: ", crono, end="\r") #Impresión simultánea
    time.sleep(1) #Tiempo que se mantiene detenido el programa cada vuelta
    total_seconds -= 1 #Ajuste del temporizador -1
    i+=1 #Ajuste del cronómetro +1
print("Hola mundo")
