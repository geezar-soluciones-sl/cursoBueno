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
    