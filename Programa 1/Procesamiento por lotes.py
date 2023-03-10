import os, time, datetime, math

print("Bienvenido a la simulación de procesamiento por lotes")


class Proceso:
    def __init__(self, nombreP, operacion, TME, id, resultado, lote):
        self.nombreP = nombreP
        self.operacion = operacion
        self.TME = TME
        self.id = id
        self.resultado = resultado
        self.lote = lote

    def __repr__(self):
        return f"Nombre del programador: {self.nombreP}, Operacion: {self.operacion}, TME: {self.TME}, ID: {self.id}"


listaID = []
listaProcesos = []
procesosPendientes = []
enProceso = []
procesosTerminados = []
"""
while True:
    print("Procesos capturados: ", len(listaProcesos))
    print("\n")
    nombreP = input("Nombre del programador: ")

    opcion = int(
        input("Operación a realizar: \n1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Residuo \nElige: "))
    while (not (opcion >= 1 and opcion <= 5)):
        print("Opción no válida")
        opcion = int(input(
            "Operación a realizar: \n1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Residuo \nElige: "))
    if (opcion == 1):
        primer = (input("Primer operando: "))
        segundo = (input("Segundo operando: "))
        operacion = primer + " + " + segundo
        primer = int(primer)
        segundo = int(segundo)
        resultado = primer + segundo
    elif (opcion == 2):
        primer = (input("Primer operando: "))
        segundo = (input("Segundo operando: "))
        operacion = primer + " - " + segundo
        primer = int(primer)
        segundo = int(segundo)
        resultado = primer - segundo
    elif (opcion == 3):
        primer = (input("Primer operando: "))
        segundo = (input("Segundo operando: "))
        operacion = primer + " * " + segundo
        primer = int(primer)
        segundo = int(segundo)
        resultado = primer * segundo
    elif (opcion == 4):
        primer = int(input("Primer operando: "))
        segundo = int(input("Segundo operando: "))
        while (segundo <= 0):
            print("Segundo operando no válido, ingrese un valor mayor a 0")
            segundo = int(input("Segundo operando: "))
        resultado = primer / segundo
        primer = str(primer)
        segundo = str(segundo)
        operacion = primer + " / " + segundo
    elif (opcion == 5):
        primer = int(input("Primer operando: "))
        segundo = int(input("Segundo operando: "))
        while (segundo <= 0):
            print("Segundo operando no válido, ingrese un valor mayor a 0")
            segundo = int(input("Segundo operando: "))
        resultado = primer % segundo
        primer = str(primer)
        segundo = str(segundo)
        operacion = primer + " % " + segundo

    TME = int(input("Tiempo máximo estimado: "))
    while (TME <= 0):
        TME = int(input("Tiempo maximo estimado no valido, ingrese un valor diferente: "))

    id = input(("Identificador de operacion: "))
    while id in listaID:
        print("El ID ya existe")
        id = input(("Identificador de operacion: "))
    listaID.append(id)
    ProcesoCap = Proceso(nombreP, operacion, TME, id, resultado, 0)
    listaProcesos.append(ProcesoCap)
    ###
    reCapturar = int(input("¿Deseas ingresar otro proceso? \n1.Sí \n2. No \nElige: "))
    if (reCapturar == 2):
        break
    while (reCapturar != 2 and reCapturar != 1):
        print("Opción incorrecta")
        reCapturar = int(input("¿Deseas ingresar otro proceso? \n1.Sí \n2. No \nElige: "))
    os.system('cls')
    # print("Proceso1: ", Proceso1)

#for proceso in listaProcesos:
    #print("Proceso: ", proceso)

# print("Proceso1: ", Proceso1)
"""

proceso1 = Proceso("aaaa", "15 + 12", 6, "1", "27", 0)
proceso2 = Proceso("bbbb", "100 - 52", 6, "2", "48", 0)
proceso3 = Proceso("cccc", "12 * 10", 6, "3", "120", 0)
proceso4 = Proceso("dddd", "15 / 5", 6, "4", "3.0", 0)
proceso5 = Proceso("eeee", "169 % 13", 6, "5", "0", 0)
proceso6 = Proceso("ffff", "56 + 74", 6, "6", "130", 0)
proceso7 = Proceso("gggg", "98 - 12", 6, "7", "86", 0)
proceso8 = Proceso("hhhhh", "56 * 87", 6, "8", "4872", 0)
proceso9 = Proceso("iiii", "36 / 4", 6, "9", "9.0", 0)


listaProcesos.append(proceso1)
listaProcesos.append(proceso2)
listaProcesos.append(proceso3)
listaProcesos.append(proceso4)
listaProcesos.append(proceso5)
listaProcesos.append(proceso6)
listaProcesos.append(proceso7)
listaProcesos.append(proceso8)
listaProcesos.append(proceso9)

cont = len(listaProcesos)
tiempoTotal = 0
NoLote = 1 

os.system("cls")
while(len(listaProcesos) > 0):
    while(len(procesosPendientes) < 4):
        procesosPendientes.append(listaProcesos.pop(0))
        if(len(listaProcesos) == 0):
            break
    print("------------------------------------------------")
    #input("Press Enter to continue...")
    for i in range(len(procesosPendientes)):
        print("Procesos en lote actual: \n")
        print ("{:<15} {:<25}".format('Nombre','TME'))  
        print()
        enProceso.append(procesosPendientes.pop(0))   
        for proceso in procesosPendientes:
            print("{:<16} {:<25}".format(proceso.nombreP, proceso.TME))

        print("------------------------------------------------")
        #enProceso.append(procesosPendientes.pop(0))
        enProceso[0].lote = NoLote
        print("Proceso realizandose: \n")
        total_seconds = enProceso[0].TME
        i=0
        print("{:<12} {:<15} {:<8} {:<8}".format('Nombre','Operacion', 'TME', 'ID'))
        print()
        print("{:<15} {:<13} {:<7} {:<8}".format(enProceso[0].nombreP,enProceso[0].operacion, enProceso[0].TME, enProceso[0].id))
        #print("Nombre: \t", enProceso[0].nombreP)
        #print("Operacion: \t", enProceso[0].operacion)
        #print("TME: \t\t", enProceso[0].TME)
        #print("ID: \t\t", enProceso[0].id)
       #procesosTerminados.append(enProceso.pop(0))
        print()
        print("------------------------------------------------")
        print("Procesos Terminados: \n")
        print("{:<12} {:<12} {:<15} {:<8}".format('Lote' ,'ID','Operacion', 'Resultado'))
        print()
        for proceso in procesosTerminados:
            print("{:<12} {:<15} {:<16} {:<7}".format(proceso.lote ,proceso.id, proceso.operacion, proceso.resultado))
            #print(proceso.id, "\t  ", proceso.operacion, "\t\t", proceso.resultado)
        print("\n")
        lotes = len(listaProcesos) / 4
        lotes = math.ceil(lotes)
        print("Número de lotes restantes: ", lotes)
        while total_seconds > 0:
            timer = datetime.timedelta(seconds = total_seconds)
            crono = datetime.timedelta(seconds = i)
            total = datetime.timedelta(seconds = tiempoTotal)
            print("Tiempo restante de proceso: ", timer, "\tTiempo transcurrido de proceso: ", crono, "\tTiempo total transcurrido: ", total, end="\r")
            time.sleep(1)
            total_seconds -= 1
            i+=1
            tiempoTotal += 1
            #os.system("cls")
        #input("Press Enter to continue...")
        procesosTerminados.append(enProceso.pop(0))
        if len(listaProcesos) == 0:
            os.system("cls")
            print("Procesos en lote actual: \n")
            print ("{:<15} {:<25}".format('Nombre','TME'))
            print("------------------------------------------------")
            print("Proceso realizandose: \n")
            print("{:<12} {:<15} {:<8} {:<8}".format('Nombre','Operacion', 'TME', 'ID'))
            print("------------------------------------------------")
            print("Procesos Terminados: \n")
            print("{:<12} {:<12} {:<15} {:<8}".format('Lote' ,'ID','Operacion', 'Resultado'))
            print()
            for proceso in procesosTerminados:
                print("{:<12} {:<15} {:<16} {:<7}".format(proceso.lote ,proceso.id, proceso.operacion, proceso.resultado))
        print("\n")
        if(len(procesosTerminados) % 4 == 0):
            NoLote += 1
        if cont > 1:
            os.system("cls")
        cont-=1


