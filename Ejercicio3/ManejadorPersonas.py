from ClasePersona import Persona
class ManejaPersona:
    __listaPers=None
    def __init__(self):
        self.__listaPers=[]

    def AgregaPers(self, pers):
        self.__listaPers.append(pers)

    def BuscaPersona(self,dni):
        i=0
        band=False
        while((band==False) and (i < len(self.__listaPers))):
            if(self.__listaPers[i].getDNI() == dni):
                band=True
            else:
                i+=1

        if(band==True):
            return i
        else:
            return -1
    