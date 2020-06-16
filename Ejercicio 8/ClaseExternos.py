from ClaseEmpleadoTemporal import Temporal
class Externos(Temporal):
    __Tarea=""
    __Viatico=0
    __CostoObra=0
    __Seguro=0
        
    def getTarea(self):
        return self.__Tarea
    def getFinTarea(self):
        return super().getFeFin()
    def getMonto(self):
        return self.__CostoObra
    def getNom(self):
        return super().getNom()
    def setViatico(self,nuevo):
        self.__Viatico=nuevo

    def __init__(self,dni,nom,dir,tel,tarea,inicio,fin,viatico,obra,seguro):
        super().__init__(dni,nom,dir,tel,inicio,fin)
        self.__Tarea=tarea
        self.__Viatico=viatico
        self.__CostoObra=obra
        self.__Seguro=seguro

    def Sueldo(self):
        total= float(self.__CostoObra) - float(self.__Viatico) - float(self.__Seguro)
        return total
    def MuestraDatos(self):
        print("***** Empleado Externo *****")
        super().MuestraDatos()
    def getTel(self):
        return super().getTel()