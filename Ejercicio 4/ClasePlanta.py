from ClaseEmpleados import Empleados
class Planta(Empleados):
    __SueldoBasico=0.0
    __Antiguedad=0

    def __init__(self,dni,nom,dir,tel,sueldo,antig):
        super().__init__(dni,nom,dir,tel)
        self.__SueldoBasico=sueldo
        self.__Antiguedad=antig
    def getNom(self):
        return super().getNom()
    def getTel(self):
        return super().getTel()

    def Sueldo(self):
        total=float(self.__SueldoBasico) * int(self.__Antiguedad)
        return total
    def MuestraDatos(self,ban=False):
        print("***** Empleado de Planta *****")
        super().MuestraDatos()