import os

print("Bienvenido a la simulación de procesamiento por lotes")


class Proceso:
    def __init__(self, nombreP, operacion, TME, id, resultado):
        self.nombreP = nombreP
        self.operacion = operacion
        self.TME = TME
        self.id = id
        self.resultado = resultado

    def __repr__(self):
        return f"Nombre del programador: {self.nombreP}, Operacion: {self.operacion}, TME: {self.TME}, ID: {self.id}"


listaID = []
listaProcesos = []
procesosPendientes = []
enProceso = []
procesosTerminados = []

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

    id = input(("Identificador de operacion: "))
    while id in listaID:
        print("El ID ya existe")
        id = input(("Identificador de operacion: "))
    listaID.append(id)
    ProcesoCap = Proceso(nombreP, operacion, TME, id, resultado)
    listaProcesos.append(ProcesoCap)
    ###
    reCapturar = int(input("¿Deseas ingresar otro proceso? \n1.Sí \n2. No \nElige: "))
    if (reCapturar == 2):
        break
    while (reCapturar != 2 and reCapturar != 1):
        print("Opción incorrecta")
        reCapturar = int(input("¿Deseas ingresar otro proceso? \n1.Sí \n2. No \nElige: "))
    os.system('clear')
    # print("Proceso1: ", Proceso1)

#for proceso in listaProcesos:
    #print("Proceso: ", proceso)

# print("Proceso1: ", Proceso1)

"""proceso1 = Proceso("Jose", "5+1", 5, "1", "6")
proceso2 = Proceso("Juan", "3+7", 5, "2", "10")
proceso3 = Proceso("Gabriel", "1+1", 5, "3", "2")
proceso4 = Proceso("Maria", "6+2", 5, "4", "8")
proceso5 = Proceso("Karla", "7+4", 5, "5", "11")
proceso6 = Proceso("Mauricio", "9+3", 5, "6", "12")

listaProcesos.append(proceso1)
listaProcesos.append(proceso2)
listaProcesos.append(proceso3)
listaProcesos.append(proceso4)
listaProcesos.append(proceso5)
listaProcesos.append(proceso6)"""

os.system("clear")
while(len(listaProcesos) > 0):
    while(len(procesosPendientes) < 4):
        procesosPendientes.append(listaProcesos.pop(0))
        if(len(listaProcesos) == 0):
            break

    print("------------------------------")
    input("Press Enter to continue...")
    for i in range(len(procesosPendientes)):
        print("Procesos en lote actual: \n")
        print("Nombre\t\tTME\n")     
        for proceso in procesosPendientes:
            print(proceso.nombreP,"\t\t",proceso.TME)
        print("------------------------------")
        enProceso.append(procesosPendientes.pop(0))
        print("Proceso realizandose: \n")
        print("Nombre: ", enProceso[0].nombreP)
        print("Operacion: ", enProceso[0].operacion)
        print("TME: ", enProceso[0].TME)
        print("ID: ", enProceso[0].id)
        print("TTE: ", "0")
        print("TRE: ", enProceso[0].TME)
        procesosTerminados.append(enProceso.pop(0))
        if(i == 1):
            input("Press Enter to continue...")
        print("------------------------------")
        print("Procesos Terminados: \n")
        print("ID\tOperacion\tResultado\n")
        for proceso in procesosTerminados:
            print(proceso.id, "\t  ", proceso.operacion, "\t\t", proceso.resultado)
        input("Press Enter to continue...")
        os.system("clear")
