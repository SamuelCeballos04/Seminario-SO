import os, time, datetime, math, random
from pynput import keyboard 

print("Bienvenido a la simulación de procesamiento")

class Proceso:
    def __init__(self, operacion, TME, TT, id, resultado, tLlegada, tFinalizacion, tRetorno, tRespuesta, tEspera, tServicio, tBloqueado):
        self.operacion = operacion
        self.TME = TME
        self.TR = TME
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
        self.flagEjecucion = False
        self.tamano = random.randint(6, 25)
        self.paginas = math.ceil(self.tamano/5)

    def __repr__(self):
        return f"Operacion: {self.operacion}, TME: {self.TME}, ID: {self.id}, Resultado: {self.resultado}"
    
class Frame: 
    def __init__(self, num, proceso, tamano, estado):
        self.num = num
        self.proceso = proceso
        self.tam = tamano
        self.estado = estado

listaFrames = []
control = 0
while control < 40:
    if control >= 38:
        frameAux = Frame(control, "SO", 5, True)
        listaFrames.append(frameAux)
        control+=1
    elif control < 38:
        frameAux = Frame(control, 0, 0, False)
        listaFrames.append(frameAux)
        control+=1

print("Lista Frames: ")
for pagina in listaFrames: 
    print("Frame: ", pagina.num, pagina.proceso, pagina.tam, pagina.estado)

procesosNuevos = []
procesosListos = []
enEjecucion = []
procesosBloqueados = []
procesosTerminados = []
indices = []


procesos = int(input("Ingrese el numero de procesos a trabajar: "))
quantum = int(input("Ingrese el valor del quantum: "))
while quantum <= 0 or quantum >= 15:
    print("Valor no válido, recuerda ingresar un valor mayor a 0 y menor a 15")
    quantum = int(input("Ingrese el valor del quantum: "))
tt = 0
quantum2 = 0
operaciones = ["+", "-", "*", "/", "%"]
#os.system("cls")
indiceProceso = 0

while(procesos > 0):
    indiceProceso += 1
    tme = random.randint(5, 16)
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
    indices.append(indiceProceso)
    procesosNuevos.append(procesoCap)
    procesos -= 1

for proceso in procesosNuevos:
    print("Proceso: ", proceso.id, proceso.operacion, proceso.TME, proceso.tamano, proceso.paginas)

def disponibles():
    disp = 0
    for frame in listaFrames: 
        if frame.estado == False:
            disp += 1
    return disp

print("Disponibles: ", disponibles())

cont = len(procesosNuevos)
cont2 = cont
tiempoTotal = 0
pausa = False
flag_1 = 0
flag_2 = 0
error = 0
total = 0
totalInt = 0
tecla = False
flagE = 0
flagI = 0
'''
while(len(procesosNuevos) > 0):
    if procesosNuevos[0].paginas <= disponibles():
        auxPaginas = procesosNuevos[0].paginas
        auxTamanoProceso = procesosNuevos[0].tamano
        auxCont = 0
        print("Len lista Frames: ", len(listaFrames))
        while auxCont <= len(listaFrames):
            print("AuxCont: ", auxCont)
            if listaFrames[auxCont].estado == False:
                print("if frame.estado == False:")
                print("AuxPaginas: ", auxPaginas)
                if auxPaginas < 0:
                    listaFrames[auxCont].estado = True
                    auxPaginas -= 1
                    listaFrames[auxCont].proceso = procesosNuevos[0].id
                    if auxTamanoProceso >= 5:
                        listaFrames[auxCont].tamano = 5
                        auxTamanoProceso -= 5
                    else:
                        listaFrames[auxCont].tamano = auxTamanoProceso
                else: 
                    break
            auxCont += 1
        procesosListos.append(procesosNuevos.pop(0))
        procesosListos[0].tLlegada = totalInt'''

while(len(procesosNuevos) > 0):
    if procesosNuevos[0].paginas <= disponibles():
        auxPaginas = procesosNuevos[0].paginas
        auxTamanoProceso = procesosNuevos[0].tamano
        auxCont = 0
        while auxCont < auxPaginas:
            for frame in listaFrames:
                if auxTamanoProceso == 0:
                    break 
                if frame.estado == False:
                    frame.proceso = procesosNuevos[0].id
                    frame.estado = True
                    if auxTamanoProceso >= 5:
                        frame.tamano = 5
                        auxTamanoProceso -= 5
                    else:
                        frame.tamano = auxTamanoProceso
                        auxTamanoProceso = 0
            auxPaginas -= 1
                
                    



        procesosListos.append(procesosNuevos.pop(0))
        procesosListos[0].tLlegada = totalInt

for proceso in procesosListos:
    print("Proceso: ", proceso.id, proceso.operacion, proceso.TME, proceso.tamano, proceso.paginas)

print("Lista Frames: ")
for pagina in listaFrames: 
    print("Frame: ", pagina.num, pagina.proceso, pagina.tam, pagina.estado)

'''
def on_press(key):
    if hasattr(key, 'char'):
        if key.char == "i":
            global flag_1
            if len(procesosListos) > 0:
                enEjecucion.append(procesosListos.pop(0))
                #quantum2 = quantum 
            if len(enEjecucion) > 0:
                procesosBloqueados.append(enEjecucion.pop(0))
            flag_1 = 1
        elif key.char == "e":
            global flag_2
            global error
            if len(enEjecucion) > 0:
                enEjecucion[0].resultado = "ERROR"
                enEjecucion[0].tFinalizacion = totalInt
                enEjecucion[0].tRetorno = totalInt - enEjecucion[0].tLlegada
                enEjecucion[0].tServicio = enEjecucion[0].TT
                if(len(procesosListos) == 0):
                    procesosTerminados.append(enEjecucion.pop(0))
                    #quantum2 = quantum
                    if len(procesosNuevos) > 0:
                        procesosListos.append(procesosNuevos.pop(0))
                        procesosListos[-1].tLlegada = totalInt
                    error = 1
                else: 
                    procesosTerminados.append(enEjecucion.pop(0))
                    enEjecucion.append(procesosListos.pop(0))
                    if len(procesosNuevos) > 0:
                        procesosListos.append(procesosNuevos.pop(0))
                        procesosListos[-1].tLlegada = totalInt
                    flag_2 = 1
        elif key.char == "p":
            global pausa
            pausa = True
        elif key.char == "t":
            global tecla
            tecla = True
        elif key.char == "c":
            pausa = False
            tecla = False
        elif key.char == "n":
            indiceProceso = indices[-1] + 1
            tme = random.randint(5, 16)
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
            indices.append(indiceProceso)
            procesosNuevos.append(procesoCap)
            if(len(procesosListos)+len(procesosBloqueados) + len(enEjecucion) < 4 and len(procesosNuevos) > 0):
                procesosListos.append(procesosNuevos.pop(0))
                procesosListos[-1].tLlegada = totalInt


l = keyboard.Listener(on_press=on_press)
l.start()


#Impresión en el transcurso del programa
def mostrar():
    print("------------------------------------------------")
    
    print("Procesos listos: \n")
    print ("{:<15} {:<15} {:<15} {:<15}".format('ID', 'TME', 'TT', 'TR'))  
    print()
    for proceso in procesosListos:
        print("{:<15} {:<15} {:<15} {:<15}".format(proceso.id, proceso.TME, proceso.TT, proceso.TR))

    print("------------------------------------------------")
    print("Proceso en ejecución: \n")
    print("{:<8} {:<12} {:<15} {:<8} {:<8}".format('ID', 'Operacion', 'TME', 'TT', 'TR'))
    print()
    for proceso in enEjecucion:
        print("{:<8} {:<12} {:<15} {:<8} {:<8} ".format(proceso.id, proceso.operacion, proceso.TME, proceso.TT, proceso.TR))
    print("Quantum restante: ", quantum2)
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
    print("{:<14} {:<15} {:<8}".format('ID','Operacion', 'Resultado'))
    print()
    for proceso in procesosTerminados:
        if proceso.resultado != "ERROR":
            proceso.resultado = round(proceso.resultado, 2)
        print("{:<15} {:<16} {:<7}".format(proceso.id, proceso.operacion, proceso.resultado))
    print("\n")
    print("Número de procesos nuevos: ", len(procesosNuevos))

#Impresión al final del programa
def mostrar2():
    print("------------------------------------------------")
    print("Procesos Realizados: \n")
    print("{:<8} {:<12} {:<14} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('ID','Operacion', 'Resultado', 'TLlegada', 'TFinali', 'TRetor', 'TResp', 'TEsp', 'TServ'))
    print()
    for proceso in procesosTerminados:
        if proceso.resultado != "ERROR":
            proceso.resultado = round(proceso.resultado, 2) 
            #proceso.tServicio = proceso.TT
        #elif proceso.resultado == "ERROR": 
         #   proceso.tServicio = proceso.TT
        print("{:<7} {:<12} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(proceso.id, proceso.operacion, proceso.resultado, proceso.tLlegada, proceso.tFinalizacion, proceso.tRetorno, proceso.tRespuesta, proceso.tEspera, proceso.tServicio))
    print("\n")

def mostrar3():
    print("------------------------------------------------")
    print("Procesos nuevos: \n")
    print ("{:<6}".format('ID'))  
    print()
    for proceso in procesosNuevos:
        print("{:<6}".format(proceso.id))
    print("------------------------------------------------")
    print("Proceso listos: \n")
    print("{:<6} {:<10} {:<10} {:<10} ".format('ID', 'Operación', 'tLlegada', 'tEspera'))
    print()
    for proceso in procesosListos:
        print("{:<6} {:<10} {:<10} {:<10} ".format(proceso.id, proceso.operacion, proceso.tLlegada, proceso.tEspera))
    print()
    print("------------------------------------------------")
    print("Proceso en Ejecucion: \n")
    print("{:<6} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format('ID', 'Operación', 'tLlegada', 'tEspera', 'tServicio', 'tRespuesta', 'TR'))
    print()
    for proceso in enEjecucion:
        print("{:<6} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format(proceso.id, proceso.operacion, proceso.tLlegada, proceso.tEspera, proceso.tServicio, proceso.tRespuesta, proceso.TR))
    print("Quantum restante: ", quantum2)
    print()
    print("------------------------------------------------")
    print("Procesos bloqueados: \n")
    print("{:<6} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format('ID', 'Operación', 'tLlegada', 'tEspera', 'tServicio', 'tRespuesta', 'TRBloqueo'))
    print()
    for proceso in procesosBloqueados:
        print("{:<6} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format(proceso.id, proceso.operacion, proceso.tLlegada, proceso.tEspera, proceso.tServicio, proceso.tRespuesta, 8-proceso.tBloqueado))
    print()
    print("------------------------------------------------")
    print("Procesos Realizados: \n")
    print("{:<8} {:<12} {:<14} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<12}".format('ID','Operacion', 'Resultado', 'TLlegada', 'TFinali', 'TRetor', 'TResp', 'TEsp', 'TServ', 'Terminacion'))
    print()
    for proceso in procesosTerminados:
        if proceso.resultado != "ERROR":
            proceso.resultado = round(proceso.resultado, 2) 
            #proceso.tServicio = proceso.TT
            terminacion = "NORMAL"
        elif proceso.resultado == "ERROR": 
            #proceso.tServicio = proceso.TT
            terminacion = "ERROR" 
        print("{:<8} {:<12} {:<14} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<12}".format(proceso.id, proceso.operacion, proceso.resultado, proceso.tLlegada, proceso.tFinalizacion, proceso.tRetorno, proceso.tRespuesta, proceso.tEspera, proceso.tServicio, terminacion))
    print("\n")


while(len(procesosNuevos) > 0):
    if procesosNuevos[0].paginas <= disponibles():
        procesosListos.append(procesosNuevos.pop(0))
        procesosListos[0].tLlegada = totalInt
quantum2 = quantum
while(cont2 > 0):
    for i in range(len(procesosListos)):
        if(len(procesosListos) > 0):
            enEjecucion.append(procesosListos.pop(0))
            total_seconds = enEjecucion[0].TR
            tt = enEjecucion[0].TT
        #while total_seconds > 0 or len(procesosBloqueados) > 0:
        #while enEjecucion[0].TME > 0 or len(procesosBloqueados) > 0:
        while len(enEjecucion) > 0 or len(procesosBloqueados) > 0:
            if len(enEjecucion) > 0:
                enEjecucion[0].tServicio += 1
                if enEjecucion[0].flagEjecucion == False:
                    enEjecucion[0].tRespuesta = totalInt - enEjecucion[0].tLlegada
                    enEjecucion[0].flagEjecucion = True
            mostrar()
            if len(enEjecucion) == 0 and len(procesosListos) > 0: #Cuando aún hay procesos en bloqueados y no en ejecución
                enEjecucion.append(procesosListos.pop(0))
            total = datetime.timedelta(seconds = tiempoTotal)
            print("Tiempo total transcurrido: ", total, end="\r")
            time.sleep(1)
            #total_seconds -= 1
            if len(enEjecucion) > 0:
                enEjecucion[0].TR -=1
                enEjecucion[0].TT +=1
            for proceso in procesosListos: #Aumenta el tiempo de espera cada segundo
                proceso.tEspera += 1
            #tt += 1
            tiempoTotal += 1
            totalInt += 1
            if len(enEjecucion) > 0:
                quantum2 -= 1 
            if len(enEjecucion) == 0 and len(procesosListos) == 0:
                quantum2 = quantum
            if quantum2 == 0:
                if(len(enEjecucion) != 0 and enEjecucion[0].TR == 0):
                    quantum2 = quantum     
                    enEjecucion[0].tFinalizacion = totalInt
                    enEjecucion[0].tRetorno = enEjecucion[0].tFinalizacion - enEjecucion[0].tLlegada
                    procesosTerminados.append(enEjecucion.pop(0))
                    cont2 -= 1
                else:
                    procesosListos.append(enEjecucion.pop(0))
                    quantum2 = quantum
                
            if len(procesosBloqueados) > 0:
                for proceso in procesosBloqueados:
                    proceso.tBloqueado += 1
                    proceso.tEspera += 1
                    if proceso.tBloqueado == 8:
                        proceso.tBloqueado = 0
                        procesosListos.append(procesosBloqueados.pop(0))
            
            while pausa:
                os.system("cls")
                mostrar()
                total = datetime.timedelta(seconds = tiempoTotal)
                print("Tiempo total transcurrido: ", total, end="\r")
                time.sleep(1)
            while tecla:
                os.system("cls")
                mostrar3()
                total = datetime.timedelta(seconds = tiempoTotal)
                print("Tiempo total transcurrido: ", total, end="\r")
                time.sleep(1)
            if(flag_1 == 1):
                if len(enEjecucion) > 0:
                    total_seconds = enEjecucion[0].TR
                    tt = enEjecucion[0].TT
                    quantum2 = quantum
                    flag_1 = 0
            if(flag_2 == 1):
                quantum2 = quantum
                cont2 -= 1
                flag_2 = 0
            if(error == 1):
                cont2 -= 1
                error = 0
            os.system("cls")
            if(len(enEjecucion) != 0 and enEjecucion[0].TR == 0):
                quantum2 = quantum     
                enEjecucion[0].tFinalizacion = totalInt
                enEjecucion[0].tRetorno = enEjecucion[0].tFinalizacion - enEjecucion[0].tLlegada
                procesosTerminados.append(enEjecucion.pop(0))
                cont2 -= 1
                if len(procesosListos) > 0:
                    enEjecucion.append(procesosListos.pop(0))
                if len(procesosNuevos) > 0:
                    procesosListos.append(procesosNuevos.pop(0))
                    procesosListos[-1].tLlegada = totalInt
        
mostrar()
mostrar2()
print("Tiempo total transcurrido: ", total)
'''