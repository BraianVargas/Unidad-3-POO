from zope.interface import implementer
from ClaseNodo import Nodo
from Interfaz import IColeccion
from ClaseVehiculo import Vehiculo
from ClaseUsado import Usado
from ClaseNuevo import Nuevo
import os
import time


@implementer(IColeccion)
class ListaVehiculo:
    __comienzo=None
    __actual=None 
    __indice=0
    __tope=0
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
    def AgregarVehiculo(self,vehiculo):
        try:
            if(type(vehiculo)==Usado or type(vehiculo)==Nuevo):
                nodo=Nodo(vehiculo)
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
                print ("*** VEHICULO AGREGADO CON EXITO ***")   
                time.sleep(1)
            else:
                raise TypeError()
        except TypeError:
            print('No es un vehiculo')     
   
    def toJson(self):
        vehiculos=[]
        for v in self:
            vehiculos.append(v.toJson())
        dic=dict(__class__=self.__class__.__name__,datos=vehiculos)
        return dic
    def InsertarElemento(self,pos,elemento):
        try:
            if(pos<self.__tope):
                nodo=Nodo(elemento)
                if(pos==0):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__tope+=1
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
                print ("*** VEHICULO INSERTADO CON EXITO ***")   
                time.sleep(1)
            else:
                    raise IndexError()
        except IndexError:
            print('Posicion Fuera De Rango')
            time.sleep(1)

    def MostrarElemento(self,elemento):
        try:
            if(type(elemento)==int):
                    if(elemento==0):
                        return 'Vehiculo '+self.__comienzo.getNombreClase()
                    else:
                        aux=self.__comienzo.getSiguiente()
                        cont=1
                        encontrado=False
                        while(aux and not encontrado):
                            if(cont==elemento):
                                encontrado=True
                            else:
                                aux=aux.getSiguiente()
                                cont+=1              
                        if(encontrado):
                            return 'Vehiculo '+aux.getNombreClase()
                        else:
                            raise IndexError      
            else:
                    if(type(elemento)==str):
                        if(isinstance(self.__comienzo.getDato(),Usado)):
                            if(self.__comienzo.getDato().getPatente().lower() == elemento.lower()):
                                pb=int(input('Precio Base: '))
                                self.__comienzo.getDato().setPrecioBase(pb)
                                return self.__comienzo.getDato()
                            else:
                                aux=self.__comienzo.getSiguiente()
                                band=False
                                while(aux!=None and band==False):
                                    if(type(aux.getDato())==Usado):
                                        if(aux.getDato().getPatente().lower()==elemento.lower()):
                                            band=True
                                        else:
                                            aux=aux.getSiguiente()
                                    else:
                                        aux=aux.getSiguiente()
                                if(band):
                                    pb=int(input('Precio Base: '))
                                    aux.getDato().setPrecioBase(pb)
                                    return aux.getDato()
                                else:
                                    return 0
                        else:
                            aux=self.__comienzo.getSiguiente()
                            band=False
                            while(aux!=None and band==False):
                                if(type(aux.getDato())==Usado):
                                    if(aux.getDato().getPatente().lower()==elemento.lower()):
                                        band=True
                                    else:
                                        aux=aux.getSiguiente()
                                else:
                                    aux=aux.getSiguiente()
                            if(band):
                                pb=int(input('Precio Base: '))
                                aux.getDato().setPrecioBase(pb)
                                return aux.getDato()
                            else:
                                return 0
        except AttributeError:
            print("No es de clase Usado")
        except IndexError:
            print('Posicion No Valida')                                     
            time.sleep(1)

    def Minimo(self):
            auto=None
            minimo=99999999
            for vehiculo in self:
                valor=vehiculo.CalcPrecioVenta()
                if(valor<minimo):
                    minimo=valor
                    auto=vehiculo
            return auto
    def Mostrar(self):
        print('-----------------------------------------')
        for vehiculo in self:
            print('{}'.format(vehiculo.getModelo()))
            print('{} Puertas'.format(vehiculo.getPuertas()))
            print('$ {}'.format(vehiculo.CalcPrecioVenta()))
            print('-----------------------------------------')
            print('\n')
