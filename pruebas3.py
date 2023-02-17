import os, time, datetime, math, random
from pynput import keyboard 

print("Bienvenido a la simulación de procesamiento por lotes")


class Proceso:
    def __init__(self, operacion, TME, TT, id, resultado, lote):
        self.operacion = operacion
        self.TME = TME
        self.TT = TT
        self.id = id
        self.resultado = resultado
        self.lote = lote

    def __repr__(self):
        return f"Operacion: {self.operacion}, TME: {self.TME}, ID: {self.id}, Resultado: {self.resultado}"

def on_press(key):
    if hasattr(key, 'char'):
        if key.char == "i":
            global flag_1
            enProceso[0].TT = tt
            enProceso[0].TME = total_seconds
            procesosPendientes.append(enProceso.pop(0))
            enProceso.append(procesosPendientes.pop(0))
            flag_1 = 1
        elif key.char == "e":
            global flag_2
            enProceso[0].resultado = "ERROR"
            procesosTerminados.append(enProceso.pop(0))
            enProceso.append(procesosPendientes.pop(0))
            flag_2 = 1
        elif key.char == "p":
            global pausa
            pausa = True
        elif key.char == "c":
            pausa = False

def mostrar():
    print("------------------------------------------------")
    
    print("Procesos en lote actual: \n")
    print ("{:<15} {:<15} {:<15}".format('ID', 'TME', 'TT'))  
    print()
    for proceso in procesosPendientes:
        print("{:<16} {:<15} {:<16}".format(proceso.id, proceso.TME, proceso.TT))

    print("------------------------------------------------")
    print("Proceso realizandose: \n")
    print("{:<12} {:<15} {:<8} {:<8}".format('Operacion', 'TME', 'TT', 'ID'))
    print()
    for proceso in enProceso:
        print("{:<13} {:<15} {:<7} {:<7}".format(proceso.operacion, total_seconds, tt, proceso.id))
    print()
    print("------------------------------------------------")
    print("Procesos Terminados: \n")
    print("{:<12} {:<14} {:<15} {:<8}".format('Lote' ,'ID','Operacion', 'Resultado'))
    print()
    for proceso in procesosTerminados:
        if proceso.resultado != "ERROR":
            proceso.resultado = round(proceso.resultado, 2)
        print("{:<12} {:<15} {:<16} {:<7}".format(proceso.lote ,proceso.id, proceso.operacion, proceso.resultado))
    print("\n")
    print("Número de lotes restantes: ", lotes)


l = keyboard.Listener(on_press=on_press)
l.start()


listaID = []
listaProcesos = []
procesosPendientes = []
enProceso = []
procesosTerminados = []

procesos = int(input("Ingrese el numero de procesos a trabajar: "))
indiceProceso = 0
tt = 0
operaciones = ["+", "-", "*", "/", "%"]
os.system("cls")


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

    procesoCap = Proceso(operacion, tme, tt, indiceProceso, res, 0)
    listaProcesos.append(procesoCap)
    procesos -= 1

cont = 1
lote = 1
for proceso in listaProcesos:
    proceso.lote = lote
    if cont == 4:
        lote+=1
        cont = 0
    cont += 1

cont = len(listaProcesos)
tiempoTotal = 0
pausa = False
flag_1 = 0
flag_2 = 0

while(len(listaProcesos) > 0):
    while(len(procesosPendientes) < 4):
        procesosPendientes.append(listaProcesos.pop(0))
        if(len(listaProcesos) == 0):
            break
    for i in range(len(procesosPendientes)):
        if(len(procesosPendientes) != 0):
            enProceso.append(procesosPendientes.pop(0))   
            total_seconds = enProceso[0].TME
            tt = enProceso[0].TT
            lotes = len(listaProcesos) / 4
            lotes = math.ceil(lotes)
        while total_seconds > 0:
            mostrar()
            total = datetime.timedelta(seconds = tiempoTotal)
            print("Tiempo total transcurrido: ", total, end="\r")
            time.sleep(1)
            total_seconds -= 1
            tt += 1
            tiempoTotal += 1
            while pausa:
                os.system("cls")
                mostrar()
                total = datetime.timedelta(seconds = tiempoTotal)
                print("Tiempo total transcurrido: ", total, end="\r")
                time.sleep(1)
                tiempoTotal += 1
            if(flag_1 == 1):
                total_seconds = enProceso[0].TME
                tt = enProceso[0].TT
                flag_1 = 0
            if(flag_2 == 1):
                total_seconds = enProceso[0].TME
                tt = enProceso[0].TT
                flag_2 = 0
            os.system("cls")
        if(len(enProceso) != 0):    
            procesosTerminados.append(enProceso.pop(0))
        cont -= 1
            
mostrar()
print("Tiempo total transcurrido: ", total)
        

