import time, os, random
from pynput import keyboard 
band = True
def on_press(key):
    if key == keyboard.Key.esc:
        global band
        band = False
        print("Presionaste esc")

l = keyboard.Listener(on_press=on_press)
l.start()

a = 0
e = 0
band2 = False
lista = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

def imprimir(): 
    print(lista)

def header():
    print('{:^150}'.format('************************\n'))
    print('{:^150}'.format('* PRODUCTOR-CONSUMIDOR *\n'))
    print('{:^150}'.format('************************\n'))
    print()

while band==True:
    if a == 22:
        a = 0
    if e == 22:
        e = 0
    num = random.randint(1, 2)
    cant = random.randint(3, 6)
    #print("Cantidad de o: ", lista.count("o"))
    #print("Cantidad de _: ", lista.count("_"))
    if band2 == False:
        #print("Productor: entrando")
        #print("Consumidor: dormido")
        aux = 0
        indice = a
        aux2 = cant
        while aux<cant:
            header()
            print()
            print('{:^150}'.format('Productor: trabajando\n'))
            print('{:^150}'.format('Consumidor: dormido\n'))
            print('{:^150}'.format('Cantidad restante a producir: ' + str(aux2)))
            print("\n\n")
            if band == False: 
                os.system("cls")
                print("Terminando proceso...")
                time.sleep(2)
                break
            if indice == 22:
                indice = 0
            lista[indice] = "o"
            lista_c = ' '.join(map(str, lista))
            print('{:^150}'.format(lista_c))
            aux += 1
            indice += 1
            aux2 -= 1
            time.sleep(0.8)
            os.system("cls")
        a = indice
        band2 = True
    if num == 1 and lista.count("_") >= cant:
        #print("Productor: entrando")
        #print("Consumidor: dormido")
        aux = 0
        indice = a
        aux2 = cant
        os.system("cls")
        while aux<cant:
            header()
            print()
            print('{:^150}'.format('Productor: trabajando\n'))
            print('{:^150}'.format('Consumidor: dormido\n'))
            print('{:^150}'.format('Cantidad restante a producir: ' + str(aux2)))
            print("\n\n")
            if band == False: 
                os.system("cls")
                print("Terminando proceso...")
                time.sleep(2)
                break
            if indice == 22:
                indice = 0
            lista[indice] = "o"
            lista_c = ' '.join(map(str, lista))
            print('{:^150}'.format(lista_c))
            aux += 1
            indice += 1
            aux2 -= 1
            time.sleep(0.8)
            os.system("cls")
        a = indice
    if num == 1 and lista.count("_") < cant:
        header()
        print()
        print('{:^150}'.format("Productor: no pudo entrar\n"))
        print('{:^150}'.format("Consumidor: dormido\n"))
        print('{:^150}'.format("Repitiendo proceso..."))
        time.sleep(1.5)
        os.system("pause")
        pass
    if num == 2 and lista.count("o") >= cant:
        #print("Productor: dormido")
        #print("Consumidor: entrando")
        aux = 0
        indice = e
        aux2 = cant
        os.system("cls")
        while aux<cant:
            header()
            print()
            print('{:^150}'.format("Productor: dormido\n"))
            print('{:^150}'.format("Consumidor: trabajando\n"))
            print('{:^150}'.format("Cantidad restante a consumir: " + str(aux2)))
            print("\n\n")
            if indice == 22:
                indice = 0
            if band == False: 
                os.system("cls")
                print("Terminando proceso...")
                time.sleep(2)
                break
            lista[indice] = "_"
            lista_c = ' '.join(map(str, lista))
            print('{:^150}'.format(lista_c))
            aux += 1
            indice += 1
            aux2 -= 1
            time.sleep(0.8)
            os.system("cls")
        e = indice
    if num == 2 and lista.count("o") < cant:
        header()
        print()
        print('{:^150}'.format("Productor: dormido\n"))
        print('{:^150}'.format("Consumidor: no pudo entrar\n"))
        print('{:^150}'.format("Repitiendo proceso..."))
        time.sleep(1.2)
        os.system("pause")
        pass
    #time.sleep(0.1)
    os.system("cls")
