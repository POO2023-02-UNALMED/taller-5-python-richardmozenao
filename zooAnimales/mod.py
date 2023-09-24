# from anfibio import Anfibio
# from ave import Ave
# from mamifero import Mamifero
# from pez import Pez
# from reptil import Reptil

def cantidadPorTipo():
    from anfibio import Anfibio
    from ave import Ave
    from mamifero import Mamifero
    from pez import Pez
    from reptil import Reptil
    mensaje = (
        "Mamifero: {}\n"
        "Aves: {}\n"
        "Reptiles: {}\n"
        "Peces: {}\n"
        "Anfibios: {}\n"
    ).format(Mamifero.cantidadMamiferos(), Ave.cantidadAves(), Reptil.cantidadReptiles(), Pez.cantidadPeces(), Anfibio.cantidadAnfibios())
    return mensaje

print(cantidadPorTipo())