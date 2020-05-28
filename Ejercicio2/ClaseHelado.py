class Helado:
    __gramos=0
    __sabores=[]

    def __init__(self,grs):
        self.__gramos=grs
        self.__sabores=[]

    def getGr(self):
        return self.__gramos
    
    def verSabores(self):
        i=0
        for i in range(len(self.__sabores)):
            print("|{}.      {} " .format(i+1,self.__sabores[i]) )

    def AgregaSabores(self,sabor):
        self.__sabores.append(sabor)
        print("Sabor Agregado")

    def cantGramos(self):
        return self.__gramos

    def contSabores(self):
        sab=len(self.__sabores)
        return sab

    def BuscaxNumero(self,numero):
        i=0
        band=0
        while(i<len(self.__sabores))and band==0:
            if(int(numero) == int(self.__sabores[i].getNum())):
                band=1
            else:
                i=i+1
        if(band==1):
          return 1
        else:
          return 0