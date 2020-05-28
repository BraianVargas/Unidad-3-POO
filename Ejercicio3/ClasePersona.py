class Persona:
    __nombre=""
    __diereccion=""
    __dni=""

    def __init__(self,nom,direc,dni):
        self.__nombre=nom
        self.__diereccion=direc
        self.__dni=dni

    def getNom(self):
        return self.__nombre
    def getDNI(self):
        return self.__dni
    def getDir(self):
        return self.__diereccion
