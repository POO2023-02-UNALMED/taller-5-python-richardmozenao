#import moduloB

class Animal:
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona

    def movimiento(self):
        return "desplazarce"
    
    @classmethod
    def totalPorTipo(cls):
        mensaje = (
            "Mamifero: {}"
            "Aves: {}"
            "Reptiles: {}"
            "Peces: {}"
            "Anfibios: {}"
        ).format(Mamifero.cantidadMamiferos(), Ave.cantidadAves(), Reptil.cantidadReptiles(), Pez.cantidadPeces(), Anfibio.cantidadAnfibios())
        return mensaje
    
    def __str__(self):
        m1 = ("Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}").format(self.nombre, self.edad, self.habitat, self.genero)
        m2 = ""
        if self.zona != None:
            m2 = (", la zona en la que me ubico es {}, en el {}").format(self.zona, self.zona.getZoo())
        return m1+m2
    
    def toString(self):
        return str(self)
    
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getHabitat(self):
        return self.habitat
    
    def getZona(self):
        return self.zona
    
    def setZona(self, zona):
        self.zona = zona
    
    def getGenero(self):
        return self.genero