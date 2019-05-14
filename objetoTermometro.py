# Nuestro objeto será un termometro con opción de escalas.
# Como atrobutos, tendrá el valor y la escala, que serán 0ºC por defecto.
# Como métodos, tendrá un conversor entre Celsius y Fahrenheit.

class Termometro():
    
    def __init__(self):
        self.unidades="C"
        self.temperatura=0
        
    def conversor(self, temperatura,unidades):
        if unidades == "C":
            t = temperatura * 9 / 5 +32
            return "{} F".format(t)
        elif unidades =="F":
            t = (temperatura - 32 ) * 5 / 9
            return "{} ºC".format(t)
        else:
            return "Unidades incorrectas"
        
    def __str__(self):
        return "{}º {}".format(self.temperatura,self.unidades)
    
    