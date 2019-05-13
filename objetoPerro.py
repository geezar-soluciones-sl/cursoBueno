# Objeto Perro: Tendrá nombre, peso y edad (atributos)
# y será capaz de ladrar (ladrar será un método)

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
        self.trabajando = False
        
    def __str__(self):
        return "Mi nombre es {} y soy un perro de asistencia".format(self.nombre)
    
    def pasear(self):
        print("Vamos a dar una vuelta")
        
    def ladrar(self):
        if not self.trabajando:
            Perro.ladrar(self)
        else:
                print("No puedo ladrar, estoy trabajando")
