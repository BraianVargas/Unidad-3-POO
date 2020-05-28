from ClaseTaller import TallerCapacitacion
import numpy as np
import csv
class ManejaTaller:
    __talleres=None
    __cantidad=0

    def __init__(self, cant=1):
        self.__talleres=np.empty(cant,dtype=TallerCapacitacion)

    def CargaTaller(self):
        arch=open('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 3/2020/Practica/Ejercicio 3/Talleres.csv')
        reader=csv.reader(arch,delimiter=',')
        for linea in reader:
            if(len(linea) == 1):
                cant=int(linea[0])
                self.__talleres.resize(cant,refcheck=False)
            else:
                taller=TallerCapacitacion(int(linea[0]),linea[1],int(linea[2]),int(linea[3]))
                self.__talleres[self.__cantidad]=taller
                self.__cantidad+=1
        arch.close()

    def Mostrar(self):
        i=0
        for i in range(len(self.__talleres)):
            print("Taller {}" .format(i+1))
            print("Nombre: " + self.__talleres[i].getNom())
            print("Identificador: {}" .format(self.__talleres[i].getId()))
            print("Vacantes Disponibles: {}" .format(self.__talleres[i].getVacantes()))
            print("Monto del taller (Precio): {}" .format(self.__talleres[i].getMonto()))
            print("\n")
            i+=1
        input("Presione ENTER para continuar")
    
    def BuscaTaller(self, nom):
        i=0
        band=0
        while((i < len(self.__talleres)) and (band == 0)):
            if(self.__talleres[i].getNom()==nom):
                if(self.__talleres[i].getVacantes() !=0 ):
                    self.__talleres[i].setVacantes()
                    band=1
                else:
                    print("Vacantes Agotadas")
                    band=2
            else:
                i+=1
        if(band==1):
            return True
        else:
            return False
    def getTaller(self, nom):
        i=0
        ban=False
        while((i<len(self.__talleres)) and (ban == False)):
            if(nom == self.__talleres[i].getNom()):
                ban=True
            else:
                i+=1
        if(ban==True):
            return self.__talleres[i]
        else:
            return 0
    def NuevoInscripto(self,nom,ins):
        i=0
        band=False
        while((i < len(self.__talleres)) and (band == False)):
            if(self.__talleres[i].getNom() == nom.getNom()):
                band=True
            else:
                i+=1
        if(band==True):
            self.__talleres[i].addInscrip(ins)

    def BuscaxNom(self, nom):
        i=0
        ban=False
        while((i < len(self.__talleres)) and (ban == False)):
            if(self.__talleres[i].getNom()==nom):
                ban=True
                self.Muestra(i)
            else:
                i+=1
    
    def VerInscriptos(self,ident):
        i=0
        ban=False
        while((i< len(self.__talleres)) and (ban==False)):
            if(self.__talleres[i].getId()==ident):
                ban=True
            else:
                i+=1
        if(ban==True):
            self.__talleres[i].VerIns()
            input("Presione ENTER para continuar")

    def Muestra(self, ind):
        print("Taller: {}" .format(self.__talleres[ind].getNom()))
        print("Monto Adeudado: {}".format(self.__talleres[ind].getDeuda()))