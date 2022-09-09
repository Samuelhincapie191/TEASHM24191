#Tendencias e Innovacion en Tecnologia Agricola
minutos = input("minutos jugados?")
valorPorMinuto = input("valor por minuto?")

# se utiliza la conversion de tipo a int
# si no se hace la conversion existira un error porque trata de multiplicar strings
# calculando el valor total de los minutos jugados
total = int(minutos) * int(valorPorMinuto)
print(total)