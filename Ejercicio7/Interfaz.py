from zope.interface import Interface

class IColeccion(Interface):
    def InsertarAgente(posicion,elemento):
        pass
    def AgregarAgente(elemento):
        pass
    def MostrarAgente(posicion):
        pass