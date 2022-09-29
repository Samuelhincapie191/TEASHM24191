#Tendencias e Innovacion en Tecnologia Agricola
def calculo_salario():
    horas = input("Cual es la cantidad de horas? ")
    tarifa = input("Cual es la tarifa? ")

    if int(horas) > 40: 
        horasextra = float(horas) - 40 
        horasnoextras = int(horas) - int(horasextra)
        tarifahorasextra = int(tarifa) * 1.5
        salario = (float(horasnoextras) * float(tarifa) + float(horasextra) * float(tarifahorasextra))
    else:
        salario = (float(horas) * float(tarifa))
    print("El salario es: "+ str(salario))
    
calculo_salario()

