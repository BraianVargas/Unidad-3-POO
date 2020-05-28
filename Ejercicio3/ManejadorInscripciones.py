import numpy as np
from ClaseInscripcion import Inscripcion
class ManejaIns:
    __arre=None
    __cant=0
    __dim=5
    def __init__(self,cant=5):
        self.__arre=np.empty((cant),dtype=Inscripcion)

    def NuevaInsc(self,obj):
        if(self.__cant==self.__dim):
            self.__dim+=5
            self.__arre.resize(self.__dim)
            self.__arre[self.__cant]=obj
            self.__cant+=1
        else:
            self.__arre[self.__cant]=obj
            self.__cant+=1

    def BuscaIns(self,dni):
        i=0 
        ban=False
        while ((i < len(self.__arre)) and (ban == False)):
            res=self.__arre[i].Busca(dni)
            if(res!=False):
                ban=True
            else:
                i+=1
        if(ban==True):
            return res
        else: 
            return False
    
    def RegistraPago(self,ind):
        self.__arre[ind].ActualizaPago()
    
    def Mostrar(self):
        for i in range(len(self.__arre)):
            print(self.__arre[i])
    
    def GeneraArchivo(self):
        i=0
        ban=False
        archi=open('Inscripciones.csv','w')
        archi.write('Fecha, Pago, Persona, Taller')
        archi.write('\n')
        while(i<len(self.__arre) and ban==False):
            if(self.__arre[i]==None):
                ban=True
            else:
                fecha=str(self.__arre[i].getFecha())
                pago=str(self.__arre[i].getPago())
                pers=str(self.__arre[i].getPersona())
                taller=str(self.__arre[i].getTaller())
                archi.write(fecha + ', ')
                archi.write(pago + ', ')
                archi.write(pers + ', ')
                archi.write(taller + ', ')
                archi.write('\n')
            i+=1
        archi.close()