from ClaseEmpleadoTemporal import Temporal
class Contratados(Temporal):
    __CantHoras=0
    __ValorHora=150             # Variable de clase (EL MISMO VALOR PARA TODOS LOS OBJETOS DE LA CLASE)

    def __init__(self,dni,nom,dir,tel,inicio,fin,horas):
        super().__init__(dni,nom,dir,tel,inicio,fin)
        self.__CantHoras=horas

    def getHoras(self):
        return int(self.__CantHoras)

    def setHoras(self,nuevo):
        self.__CantHoras=nuevo
    def getDNI(self):
        dni=super().getDNI()
        return dni
    def getNom(self):
        return super().getNom()
    def Sueldo(self):
        total = float(self.__CantHoras) * float(self.__ValorHora)
        return total
    def MuestraDatos(self):
        print("***** Empleado Contratado *****")
        super().MuestraDatos()
    def getTel(self):
        return super().getTel()