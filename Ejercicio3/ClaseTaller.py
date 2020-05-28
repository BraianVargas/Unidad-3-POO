class TallerCapacitacion:
    __idTaller=0
    __nombre=""
    __vacantes=0
    __montoinscripcion=0

    __inscripciones=[]

    def __init__(self,iden,nom,vac,monto):
        self.__idTaller=iden
        self.__nombre=nom
        self.__vacantes=vac
        self.__montoinscripcion=monto
        self.__inscripciones=[]

    def getId(self):
        return int(self.__idTaller)
    def getNom(self):
        return str(self.__nombre)
    def getVacantes(self):
        return int(self.__vacantes)
    def setVacantes(self):
        self.__vacantes=int(self.__vacantes)-1
    def getMonto(self):
        return int(self.__montoinscripcion)
    
    def getDeuda(self):
        i=a=0
        ban=False
        while((i<len(self.__inscripciones)) and ban==False):
            if(self.__inscripciones[i].getPago()==True):
                a = 0
            else:
                a = self.getMonto()
            i+=1
        return a

    def addInscrip(self, ins):
        self.__inscripciones.append(ins)

    def VerIns(self):
        i=0
        ban=False
        while((i< len(self.__inscripciones)) and (ban==False)):
            if(self.__inscripciones[i]==None):
                ban=True
            else:
                print("*** Inscripto N° {} ***\n {}".format(i+1, self.__inscripciones[i]))
                i+=1
                