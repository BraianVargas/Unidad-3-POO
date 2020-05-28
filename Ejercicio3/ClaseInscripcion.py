import datetime
class Inscripcion:
    __fechainscripcion=datetime
    __pago=bool
    __persona=None
    __taller=None

    def __init__(self,fecha,pago,persona,taller):
        self.__fechainscripcion=fecha
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller

    def __str__(self):
        s=("Fecha de Insc.: {}\nPago: {}\nPersona: {}\n" .format(self.__fechainscripcion, self.__pago,self.__persona.getNom()))
        return s

    def MuestraTaller(self):
        print("Taller: {}" .format(self.__taller.getNom()))

    def Busca(self, dni):
        if(self.__persona.getDNI()== dni):
            return self.__taller.getNom()
        else:
            return False
    def ActualizaPago(self):
        self.__pago=True
    
    def getFecha(self):
        return self.__fechainscripcion
    def getPago(self):
        return self.__pago
    def getPersona(self):
        a=(" {} {} {}" .format(self.__persona.getNom(), self.__persona.getDNI(),self.__persona.getDir()))
        return a
    def getTaller(self):
        a=("{} {}" .format(self.__taller.getId(),self.__taller.getNom()))
        return a