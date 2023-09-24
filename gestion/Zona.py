class Zona:
    def __init__(self, nombre, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)
        animal.setZona(self)

    def cantidadAnimales(self):
        return len(self.animales)
    
    def getNombre(self):
        return self.nombre
    
    def getZoo(self):
        return self.zoo
    
    def getAnimales(self):
        return self.animales
