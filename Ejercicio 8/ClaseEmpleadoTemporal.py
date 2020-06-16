from ClaseEmpleados import Empleados
class Temporal(Empleados):
    __feInicio=0
    __feFin=0

    def getFeInicio(self):
        return self.__feInicio
    def getFeFin(self):
        return self.__feFin

    def __init__(self,dni,nom,dir,tel,feinicio,fefin):
        super().__init__(dni,nom,dir,tel)
        self.__feInicio=feinicio
        self.__feFin=fefin
    