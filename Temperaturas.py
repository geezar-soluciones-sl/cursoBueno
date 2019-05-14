
def pedirEntradaCF(mensaje):
    validez = False
    pedido=None
    while not validez:
        pedido=input(mensaje)
        if pedido.capitalize()=="F" or pedido.capitalize()=="C":
            return pedido
        else:
            print("Valor introducido no válido")
def pasarACelsius(entrada):
    return (entrada - 32 ) * 5 / 9
def pasarAFahrenheit(entrada):
    return entrada * 9 / 5 +32

valorIntro=pedirEntradaCF("Introduzca conversión a Celsius (C) o a Fahrenheit (F): ")

if valorIntro.capitalize()=="C":
    for i in range (0,24):
        print(i*10, " grados Fahrenheit equivalen a ", round(pasarACelsius(i*10),2), " grados Celsius")
else:
   for i in range (0,2):
        print(i*100, " grados Celsius equivalen a ", round(pasarAFahrenheit(i*100),2), " grados Fahrenheit")
