#Tendencias e Innovacion en Tecnologia Agricola
total = 0
contador = 0 
while True:
    cadena = input("Ingrese un número: ")
    try:
        if (cadena == "Fin"):
            break
        else:
            total = total + int(cadena)
            contador = contador + 1
            media = total / contador
    except:
        print("Valor no es valido")
        continue

print("Total: ", total)
print("Contador: ", contador)
print("Media: ", media)
