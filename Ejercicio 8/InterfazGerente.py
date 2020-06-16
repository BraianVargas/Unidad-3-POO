from zope.interface import Interface
from zope.interface import implementer

class IGerente(Interface):
    def modificarBasicoEPlanta(self,dni, nuevoBasico):
        pass
    def modificarViaticoEExterno(self,dni, nuevoViatico):
        pass
    def modificarValorEPorHora(self,dni, nuevoValorHora):
        pass