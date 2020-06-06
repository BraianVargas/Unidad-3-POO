class Vehiculo:
    __Modelo=""
    __CantPuertas=0
    __Color=""
    __PrecioBase=""

    def __init__(self,modelo,puertas,color,preciobase):
        self.__Modelo=modelo
        self.__CantPuertas=int(puertas)
        self.__Color=color
        self.__PrecioBase=int(preciobase)
    def __str__(self):
        print('Vehiculo')
        print('Modelo: {}' .format(self.__Modelo))
        print('Puertas: {}'.format(self.__CantPuertas))
        print('Color: {}'.format(self.__Color))
        print('Precio Base: {}'.format(self.__PrecioBase))
        return ""
    def toJson(self):
        pass
    def getModelo(self):
        return self.__Modelo
    def getPuertas(self):
        return self.__CantPuertas
    def getColor(self):
        return self.__Color
    def getPrecioBase(self):
        return float(self.__PrecioBase)
    def setPrecioBase(self,pb):
        self.__PrecioBase=pb