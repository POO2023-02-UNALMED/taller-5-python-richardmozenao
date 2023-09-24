class Zoologico:
    def __init__(self, nombre, ubicacion, zonas=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        c = 0
        for x in self._zonas:
            c += x.cantidadAnimales()
        return c
    
    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZonas(self):
        return self._zonas
