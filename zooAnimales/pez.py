from . import animal

class pez(animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        pez.listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return pez(nombre, edad, "oceano", genero, "rojo", 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return pez(nombre, edad, "oceano", genero, "gris", 6)
    
    @classmethod
    def getSalmones(cls):
        return cls.salmones
    
    @classmethod
    def getBacalaos(cls):
        return cls.bacalaos
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getCantidadAletas(self):
        return self.cantidadAletas
