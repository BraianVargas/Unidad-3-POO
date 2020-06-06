from zope.interface import Interface

class IColeccion(Interface):
    def insertarVehiculo(posicion,elemento):
        pass
    def agregarVehiculo(elemento):
        pass
    def mostrarVehiculos(posicion):
        pass