class Sabor:
    __numero=0
    __nombre=""
    __descripcion=""
    
    __Cont=0

    def __init__(self,num,nom,desc):
        self.__numero=num
        self.__nombre=nom
        self.__descripcion=desc
        self.__Cont=0
    
    def setCont(self):
        self.__Cont+=1
    
    def getCont(self):
        return int(self.__Cont)

    def getNom(self):
        return self.__nombre

    def getNum(self):
        return int(self.__numero)