import os, time, datetime, math, random
from pynput import keyboard 

print("Bienvenido a la simulación de procesamiento por lotes")


class Proceso:
    def __init__(self, operacion, TME, TT, id, resultado, tLlegada, tFinalizacion, tRetorno, tRespuesta, tEspera, tServicio, tBloqueado):
        self.operacion = operacion
        self.TME = TME
        self.TT = TT #Cada que el proceso está en ejecución
        self.id = id
        self.resultado = resultado
        self.tLlegada = tLlegada
        self.tFinalizacion = tFinalizacion
        self.tRetorno = tRetorno
        self.tRespuesta = tRespuesta
        self.tEspera = tEspera
        self.tServicio = tServicio
        self.tBloqueado = tBloqueado




    def __repr__(self):
        return f"Operacion: {self.operacion}, TME: {self.TME}, ID: {self.id}, Resultado: {self.resultado}"

def on_press(key):
    if hasattr(key, 'char'):
        if key.char == "i":
            global flag_1
            enEjecucion[0].TT = tt
            enEjecucion[0].TME = total_seconds
            if len(procesosListos) > 0:
                enEjecucion.append(procesosListos.pop(0))
                procesosBloqueados.append(enEjecucion.pop(0))

            flag_1 = 1
        elif key.char == "e":
            global flag_2
            global error
            enEjecucion[0].resultado = "ERROR"
            if(len(procesosListos) == 0):
               procesosTerminados.append(enEjecucion.pop(0))
               error = 1
            else: 
                procesosTerminados.append(enEjecucion.pop(0))
                enEjecucion.append(procesosListos.pop(0))
                flag_2 = 1
        elif key.char == "p":
            global pausa
            pausa = True
        elif key.char == "c":
            pausa = False

def mostrar():
    print("------------------------------------------------")
    
    print("Procesos listos: \n")
    print ("{:<15} {:<15} {:<15}".format('ID', 'TME', 'TT'))  
    print()
    for proceso in procesosListos:
        print("{:<16} {:<15} {:<16}".format(proceso.id, proceso.TME, proceso.TT))

    print("------------------------------------------------")
    print("Proceso realizándose: \n")
    print("{:<12} {:<15} {:<8} {:<8}".format('Operacion', 'TME', 'TT', 'ID'))
    print()
    for proceso in enEjecucion:
        print("{:<13} {:<15} {:<7} {:<7}".format(proceso.operacion, total_seconds, tt, proceso.id))
    print()
    print("------------------------------------------------")
    print("Procesos bloqueados: \n")
    print("{:<12} {:<15}".format('ID', 'Tiempo Bloqueado'))
    print()
    for proceso in procesosBloqueados:
        print("{:<13} {:<15}".format(proceso.id, proceso.tBloqueado))
    print()
    print("------------------------------------------------")
    print("Procesos Terminados: \n")
    print("{:<12} {:<14} {:<15} {:<8}".format('Tiempo Tr' ,'ID','Operacion', 'Resultado'))
    print()
    for proceso in procesosTerminados:
        if proceso.resultado != "ERROR":
            proceso.resultado = round(proceso.resultado, 2)
        print("{:<12} {:<15} {:<16} {:<7}".format(proceso.TT ,proceso.id, proceso.operacion, proceso.resultado))
    print("\n")
    print("Número de procesos nuevos: ", len(procesosNuevos))


l = keyboard.Listener(on_press=on_press)
l.start()

procesosNuevos = []
procesosListos = []
enEjecucion = []
procesosBloqueados = []
procesosTerminados = []

procesos = int(input("Ingrese el numero de procesos a trabajar: "))
indiceProceso = 0
tt = 0
operaciones = ["+", "-", "*", "/", "%"]
os.system("cls")


while(procesos > 0):
    indiceProceso += 1
    tme = random.randint(5, 7)
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operador = random.choice(operaciones)
    operacion = str(num1) + " " + operador + " " + str(num2)

    if(operador == "+"):
        res = num1 + num2
    elif(operador == "-"):
        res = num1 - num2
    elif(operador == "*"):
        res = num1 * num2
    elif(operador == "/"):
        res = num1 / num2
    elif(operador == "%"):
        res = num1 % num2

    procesoCap = Proceso(operacion, tme, tt, indiceProceso, res, 0, 0, 0, 0, 0, 0, 0)
    procesosNuevos.append(procesoCap)
    procesos -= 1

cont = len(procesosNuevos)
cont2 = cont
tiempoTotal = 0
pausa = False
flag_1 = 0
flag_2 = 0
error = 0

while(cont2 > 0):
    while(len(procesosListos)+len(procesosBloqueados) < 4 and len(procesosNuevos) > 0):
        procesosListos.append(procesosNuevos.pop(0))
    for i in range(len(procesosListos)):
        if(len(procesosListos) > 0):
            print("Sí entra")
            enEjecucion.append(procesosListos.pop(0))
            total_seconds = enEjecucion[0].TME
            tt = enEjecucion[0].TT
        while total_seconds > 0:
            mostrar()
            total = datetime.timedelta(seconds = tiempoTotal)
            print("Tiempo total transcurrido: ", total, end="\r")
            time.sleep(1)
            total_seconds -= 1
            tt += 1
            tiempoTotal += 1
            if len(procesosBloqueados) > 0:
                for proceso in procesosBloqueados:
                    proceso.tBloqueado += 1
                    if proceso.tBloqueado == 8:
                        proceso.tBloqueado = 0
                        procesosListos.append(procesosBloqueados.pop(0))

            while pausa:
                os.system("cls")
                mostrar()
                total = datetime.timedelta(seconds = tiempoTotal)
                print("Tiempo total transcurrido: ", total, end="\r")
                time.sleep(1)
                tiempoTotal += 1
            if(flag_1 == 1):
                total_seconds = enEjecucion[0].TME
                tt = enEjecucion[0].TT
                flag_1 = 0
            if(flag_2 == 1):
                total_seconds = enEjecucion[0].TME
                tt = enEjecucion[0].TT
                flag_2 = 0
            if(error == 1):
                total_seconds = 0
                tt = 0
                error = 0
            os.system("cls")
        if(len(enEjecucion) != 0):    
            procesosTerminados.append(enEjecucion.pop(0))
            cont2 -= 1
            if len(procesosNuevos) != 0:
                procesosListos.append(procesosNuevos.pop(0))
            
mostrar()
print("Tiempo total transcurrido: ", total)
        

