from . import animal

class anfibio(animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        anfibio.listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado())
    
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return anfibio(nombre, edad, "selva", genero, "rojo", True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    
    @classmethod
    def getRanas(cls):
        return cls.ranas
    
    @classmethod
    def getSalamandras(cls):
        return cls.salamandras
    
    def getColorPiel(self):
        return self.colorPiel
    
    def isVenenoso(self):
        return self.venenoso
    
