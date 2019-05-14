# Nuestro objeto será un termometro con opción de escalas.
# Como atrobutos, tendrá el valor y la escala, que serán 0ºC por defecto.
# Como métodos, tendrá un conversor entre Celsius y Fahrenheit.
# Añadimos getters y setters.
# Añadimos método "mide" para salida en unidades concretas
# Transformamos el conversor en privado

class Termometro():
    
    def __init__(self):
        self.__unidades="C"
        self.__temperatura=0
        
    def __conversor(self, temperatura,unidades):
        if unidades == "C":
            t = temperatura * 9 / 5 +32
            return "{} ºF".format(t)
        elif unidades =="F":
            t = (temperatura - 32 ) * 5 / 9
            return "{} ºC".format(t)
        else:
            return "Unidades incorrectas"
        
    def __str__(self):
        return "{}º {}".format(self.__temperatura,self.__unidades)
    
# Ponemos getter y setter para cada atributo
    def unidadMedida(self, unidad=None):
        if unidad == None:
            return self.__unidades
        else:
            if unidad == "F" or unidad == "C":
                self.__unidades = unidad

    def temp(self, temp=None):
        if temp == None:
            return self.__temperatura
        else:
            self.__temperatura = temp
# Método para devolver la medida, con dudas o errores pasamos lo que tenemos y fuera
    def mide(self, unid=None):
        if unid == None or unid == self.__unidades:
            return self.__str__()
        else:
            if unid == "C" or unid == "F":
                return self.__conversor(self.__temperatura, self.__unidades)
            else:
                return self.__str__()
        

