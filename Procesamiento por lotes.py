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


while True: 
    print("Procesos capturados: ", len(listaProcesos))
    print("\n")
    nombreP = input("Nombre del programador: ")

    opcion = int(input("Operación a realizar: \n1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Residuo \nElige: "))
    while (not(opcion >= 1 and opcion <=5)):
        print("Opción no válida")
        opcion = int(input("Operación a realizar: \n1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Residuo \nElige: "))
    if(opcion == 1): 
        primer = (input("Primer operando: "))
        segundo = (input("Segundo operando: "))
        operacion = primer + " + " + segundo
        primer = int(primer)
        segundo = int(segundo)
        resultado = primer + segundo
    elif(opcion == 2): 
        primer = (input("Primer operando: "))
        segundo = (input("Segundo operando: "))
        operacion = primer + " - " + segundo
        primer = int(primer)
        segundo = int(segundo)
        resultado = primer - segundo
    elif(opcion == 3): 
        primer = (input("Primer operando: "))
        segundo = (input("Segundo operando: "))
        operacion = primer + " * " + segundo
        primer = int(primer)
        segundo = int(segundo)
        resultado = primer * segundo
    elif(opcion == 4): 
        primer = int(input("Primer operando: "))
        segundo = int(input("Segundo operando: "))
        while(segundo <= 0):
            print("Segundo operando no válido, ingrese un valor mayor a 0")
            segundo = int(input("Segundo operando: "))
        resultado = primer / segundo
        primer = str(primer)
        segundo = str(segundo)
        operacion = primer + " / " + segundo
    elif(opcion == 5):
        primer = int(input("Primer operando: "))
        segundo = int(input("Segundo operando: "))
        while(segundo <= 0):
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
    os.system('cls')
    #print("Proceso1: ", Proceso1)



for proceso in listaProcesos: 
    print("Proceso: ", proceso)

#print("Proceso1: ", Proceso1)
