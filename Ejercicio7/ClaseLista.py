from zope.interface import implementer
from ClaseNodo import Nodo
from Interfaz import IColeccion
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocInv import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo

import os
import time

@implementer(IColeccion)
class ListaPersonal:
    __comienzo=None
    __actual=None 
    __indice=0
    __tope=0
    def getTope(self):
        return self.__tope
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:        
            dato=self.__actual.getDato()
            self.__indice+=1  
            self.__actual=self.__actual.getSiguiente()        
            return dato
    
    def toJson(self):
        personal=[]
        for v in self:
            personal.append(v.toJson())
        dic=dict(__class__=self.__class__.__name__,datos=personal)
        return dic
    
    def mostrar(self):
        aux=self.__comienzo
        print('---------------------')
        while(aux!=None):
            print('------------------') 
            print(aux.getDato())
            aux=aux.getSiguiente()

    def AgregarAgente(self,persona):
        try:
            if(type(persona)==PersonalApoyo or type(persona)==Docente or type(persona)==Investigador or type(persona)==DocenteInvestigador):
                nodo=Nodo(persona)
                if(self.__comienzo==None):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__actual=nodo
                    self.__tope+=1
                else:
                    aux=self.__comienzo
                    while(aux.getSiguiente()!=None):
                        aux=aux.getSiguiente()
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope+=1
                os.system('cls')
                print ("*** AGENTE AGREGADO CON EXITO ***")   
                time.sleep(1)
        except TypeError:
            print('No es una persona')

    def InsertarAgente(self,pos,Agente):
        try:
            if(pos<=self.__tope):
                nodo=Nodo(Agente)
                if(pos==0):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__tope+=1
                    os.system('cls')
                    print ("*** AGENTE INSERTADO CON EXITO ***")   
                    time.sleep(1)
                else:
                    num=1
                    aux=self.__comienzo
                    while(num<pos):
                        aux=aux.getSiguiente()
                        num+=1
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope+=1    
                    os.system('cls')
                    print ("*** AGENTE INSERTADO CON EXITO ***")   
                    time.sleep(1)
        except IndexError:
            print('Posicion Fuera De Rango')
            time.sleep(1)

    def Inciso3(self,pos):
        try:
            cont=0
            aux=self.__actual
            ban=False
            if(self.__tope>=pos):
                while((pos<=self.__tope)and(ban==False) and (aux!=None)):
                    if(pos==cont):
                        ban=True
                        print("Tipo de agente: {}" .format(aux.getDato().__class__.__name__))
                    else:
                        cont+=1
                        aux=aux.getSiguiente()
                        ban=False
            else:
                raise IndexError
        except IndexError:
            os.system('cls')
            print('***Posicion Fuera De Rango***')
    def ListadoPorNombre(self,carrera):
        nombres=[]
        try:
            cont=0
            aux=self.__actual
            while((cont<=self.__tope) and (aux!=None)):
                if(isinstance(aux.getDato(),DocenteInvestigador)):
                    if(aux.getDato().getCarrera().lower()==carrera.lower()):
                        nombres.append(aux.getDato().getNombre())
                cont+=1
                aux=aux.getSiguiente()
            else:
                if(cont<=self.__tope and nombres==None):
                    os.system('cls')
                    print("No se encontraron agentes pertenecientes a la carrera.")
                    time.sleep(1.5)
            nombres.sort()
            os.system('cls')
            for i in range(len(nombres)):
                aux=self.__comienzo
                
                while(aux!=None):
                    if(nombres[i].lower()==aux.getDato().getNombre().lower() and isinstance(aux.getDato(),DocenteInvestigador) ):
                        print("*** Datos ***")
                        print(aux.getDato())
                    aux=aux.getSiguiente()

        except IndexError:
            os.system('cls')
            print('***Posicion Fuera De Rango***')
        finally:
            print("Nombres: \n{}".format(nombres))

    def inciso5(self,areainv):
        contDI=contI=0
        try:
            cont=0
            aux=self.__comienzo
            while((cont<=self.__tope) and (aux!=None)):
                if(isinstance(aux.getDato(),DocenteInvestigador)):
                    print(aux.getDato().getNombre())
                    if(aux.getDato().getAreaInv().lower()==areainv.lower()):
                        contDI+=1
                else:
                    if(isinstance(aux.getDato(),Investigador)):
                        print(aux.getDato().getNombre())
                        if(aux.getDato().getAreaInv().lower()==areainv.lower()):
                            contI+=1
                cont+=1
                aux=aux.getSiguiente()
            else:
                if(cont<=self.__tope and contDI==0 and contI==0):
                    os.system('cls')
                    print("No se encontraron agentes pertenecientes a ésta área.")
                    time.sleep(1.5)
                else:
                    print("Docentes investigadores: {}" .format(contDI))
                    print("Investigadores: {}" .format(contI))
        except IndexError:
            os.system('cls')
            print('***Posicion Fuera De Rango***')

    def OrdenaPorApellidos(self):
        try:
            k=cota=p=None
            aux=None

            while(k!=self.__comienzo):
                k=self.__comienzo
                p=self.__comienzo
                while(p.getSiguiente()!=cota):
                    if(p.getDato().getApellido().lower() > p.getSiguiente().getDato().getApellido().lower()):
                        aux=p.getSiguiente().getDato()
                        p.getSiguiente().setDato(p.getDato())
                        p.setDato(aux)
                        k=p
                    p=p.getSiguiente()
                cota=k.getSiguiente()
        except IndexError:
            os.system('cls')
            print('***Posicion Fuera De Rango***')

    def BuscaPorCategorias(self, categoria):
        acum=0
        aux=self.__comienzo
        while(aux!=None):
            if(isinstance(aux.getDato(),DocenteInvestigador)):
                if(aux.getDato().getCategoria().lower()==categoria.lower()):
                    print("\n-------------------------------")
                    print("Nombre: {}".format(aux.getDato().getNombre()))
                    print("Apellido: {}".format(aux.getDato().getApellido()))
                    print("Importe Extra: {}".format(aux.getDato().getExtra()))
                    acum+=aux.getDato().getExtra()
            aux=aux.getSiguiente()
        print("\nCantidad total de dinero a solicitar: ${}".format(acum))