# Objeto Perro: Tendrá nombre, peso y edad (atributos)
# y será capaz de ladrar (ladrar será un método)
# En perro asistencia, el método trabajando funciona como getter y setter
# (devuelve o fija según haya algo en paréntesis o no) para variables privadas (con __=

class Perro():
    def __init__(self, nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self):
        if self.peso>=8:
            print("GUAU GUAU")
        else:
            print("Guaaau")
            
    def __str__(self):
        return "Mi nombre es {}".format(self.nombre)
    
class PerroGuia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo=amo
        self.__trabajando = False
        
    def __str__(self):
        return "Mi nombre es {} y soy un perro de asistencia".format(self.nombre)
    
    def pasear(self):
        print("Vamos a dar una vuelta")
        
    def ladrar(self):
        if not self.__trabajando:
            Perro.ladrar(self)
        else:
                print("No puedo ladrar, estoy trabajando")

# GETTER / SETTER según el if

    def trabajando(self, valor=None):
        if valor==None:
            return self.__trabajando
        else:
            self.__trabajando=valor