from ClaseSabor import Sabor
import csv

class ManejaSabores:
    __liSabores=[]

    def __init__(self):
        self.__liSabores=[]

    def CargaSabores(self):
        arch=open('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 3/2020/Practica/Ejercicio 2/sabores.csv')
        reader=csv.reader(arch,delimiter=',')

        for lin in reader:
            unsabor=Sabor(lin[0],lin[1],lin[2])
            self.__liSabores.append(unsabor)
        arch.close()

    def buscaSaborxNombre(self,nom):
        ban=False
        i=0
        while (ban==False) and (i<len(self.__liSabores)):
            if((self.__liSabores[i].getNom()).lower() == nom):
                ban=True
            else:
                i+=1
        if(i==len(self.__liSabores)):
            return False
        else: 
            self.__liSabores[i].setCont()
            return True

    def SaboresmasPedidos(self,sabores):
        i=0
        populares=[]
        for i in range(len(self.__liSabores)):
            if(self.__liSabores[i].getCont()!=0):
                populares.append(self.__liSabores[i].getCont())
            i+=1
        lis=sorted(populares,reverse=True)
        return lis

    def MuestraMasPedidos(self,lis):
        li=[""]
        for i in range(len(lis)):
            x=0
            j=0
            band=False
            while( (j < len(self.__liSabores)) and (band==False)):
                    if(lis[i] == self.__liSabores[j].getCont()):
                        while(self.__liSabores[j].getNom() == li[x]):
                            band=True
                            j+=1
                        else:
                            if(len(li)<=5):
                                li.append(self.__liSabores[j].getNom())
                                x+=1
                            j+=1
                    else:
                        j+=1
        x=0
        for x in range(len(li)):
            print(li[x])
