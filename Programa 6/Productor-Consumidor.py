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
            print("Productor: trabajando")
            print("Consumidor: dormido")
            print("Cantidad restante a producir: ", aux2)
            if band == False: 
                os.system("cls")
                print("Terminando proceso...")
                time.sleep(2)
                break
            if indice == 22:
                indice = 0
            lista[indice] = "o"
            print(lista)
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
            print("Productor: trabajando")
            print("Consumidor: dormido")
            print("Cantidad restante a producir: ", aux2)
            if band == False: 
                os.system("cls")
                print("Terminando proceso...")
                time.sleep(2)
                break
            if indice == 22:
                indice = 0
            lista[indice] = "o"
            print(lista)
            aux += 1
            indice += 1
            aux2 -= 1
            time.sleep(0.8)
            os.system("cls")
        a = indice
    if num == 1 and lista.count("_") < cant:
        print("Productor: no pudo entrar")
        print("Consumidor: dormido")
        print("Repitiendo proceso...")
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
            print("Productor: dormido")
            print("Consumidor: trabajando")
            print("Cantidad restante a consumir: ", aux2)
            if indice == 22:
                indice = 0
            if band == False: 
                os.system("cls")
                print("Terminando proceso...")
                time.sleep(2)
                break
            lista[indice] = "_"
            print(lista)
            aux += 1
            indice += 1
            aux2 -= 1
            time.sleep(0.8)
            os.system("cls")
        e = indice
    if num == 2 and lista.count("o") < cant:
        print("Productor: dormido")
        print("Consumidor: no pudo entrar")
        print("Repitiendo proceso...")
        time.sleep(1.2)
        os.system("pause")
        pass
    time.sleep(0.5)
    os.system("cls")
