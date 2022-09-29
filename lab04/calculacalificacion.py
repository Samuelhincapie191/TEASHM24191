#Tendencias e Innovacion en Tecnologia Agricola
def calcula_calificacion(puntuacion):
    
    if (puntuacion >= 0.9 and puntuacion <=1):
        nota = "Sobresaliente"
    elif (puntuacion >= 0.8 and puntuacion < 0.9):
        nota = "Notable"
    elif (puntuacion >= 0.7 and puntuacion < 0.8):
        nota = "Bien"
    elif (puntuacion >= 0.6 and puntuacion < 0.7):
        nota = "Suficiente"
    elif (puntuacion >= 0 and puntuacion <= 0.6):
        nota = "Insuficiente"
    else: 
        nota = "El valor ingresado no es valido"
    return nota

try:
    puntuacion = float(input("Ingrese la calificación (0 - 1): "))
    nota = calcula_calificacion(puntuacion)
    print("El grado de su calificacion es:" , nota)
except: 
    print("Error, debe ingresar un valor númerico")