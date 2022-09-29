#Tendencias e Innovacion en Tecnologia Agricola 
maximo = 0
minimo = 0
numeroInicial = True

while True: 
    try:
        numeroIngresado = input("Ingrese un número: ")
        if (numeroIngresado == "fin"):
            break
        else:
            if (numeroInicial):
                maximo = int(numeroIngresado)
                minimo = int(numeroIngresado)
                numeroInicial = False
            else: 
                if (int(numeroIngresado) > maximo): maximo = int(numeroIngresado)
                if (int(numeroIngresado) < minimo): minimo = int(numeroIngresado)
    except:
        print("Valor no es valido")
        continue

print("Maximo: ", maximo)
print("Minimo: ", minimo)
