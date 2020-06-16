class Empleados:
    __DNI=""
    __Nombre=""
    __Direccion=""
    __Telefono=""

    def __init__(self,dni,nom,dir,tel):
        self.__DNI=dni
        self.__Nombre=nom
        self.__Direccion=dir
        self.__Telefono=tel
    def getDNI(self):
        return int(self.__DNI)
    def getNom(self):
        return self.__Nombre
    def getTel(self):
        return self.__Telefono

    def MuestraDatos(self):
        print("Nombre: {}".format(self.__Nombre))
        print("DNI: {}".format(self.__DNI))
        print("Dirección: {}".format(self.__Direccion))
        