from . import animal

class reptil(animal):
    listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        reptil.listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    @classmethod
    def getIguanas(cls):
        return cls.iguanas
    
    @classmethod
    def getSerpientes(cls):
        return cls.serpientes
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola
    
