listaID = ["5", "8", "9"]
id = input(("Identificador de operacion: "))
while id in listaID:
    print("El ID ya existe")
    id = input(("Identificador de operacion: "))

print("ID: ", id)