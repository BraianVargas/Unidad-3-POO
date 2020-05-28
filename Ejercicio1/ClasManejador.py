from ClaseLibro import Libro
from ClaseCapitulo import Capitulo
import csv
import os
import gc

class ManejaLibro:
    __listaLibros = []

    def __init__(self):
        self.__listaLibros = []

    def cargaLibros(self):
        archivo=open("C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 3/2020/Practica/Ejercicio1/Libros.csv")
        reader=csv.reader(archivo,delimiter=',')
        i=-1
        for linea in reader:
            if(len(linea)==6):
                libro=Libro(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
                self.__listaLibros.append(libro)
                i+=1
            elif (len(linea) == 2):
                Cap=Capitulo(linea[0],linea[1])
                self.__listaLibros[i].AgregaCapitulo(Cap)
        archivo.close()

    def buscarId(self,iden):
        i=0
        band=False
        while (band==False)and(i<len(self.__listaLibros)):
            if(iden==self.__listaLibros[i].getId()):
                band=True
            else:
                i=i+1
        if(band==False):
            return False
        else:
            return i+1

    def mostrarDatos(self,i):
        print("Titulo: {}" .format(self.__listaLibros[i].getTitulo()))
        print("Capitulos: ")
        print(self.__listaLibros[i].muestraCap())
        print("Cantidad total de paginas: {}" .format(self.__listaLibros[i].getTotPag()))
        input("")
    
    def buscaPalabra(self, palabra):
        ban=False
        i=j=0
        while not ban and (i<len(self.__listaLibros)):
            lib=self.__listaLibros[i].getTitulo()
            lLib=lib.split()
            while (j < len(lLib)) and (ban == False):
                if(lLib[j].lower() == palabra):
                    ban=True
                else: j+=1
            if(not ban):
                capi=self.__listaLibros[i].buscaPal(palabra)
                if(capi==True):
                    ban=True
                else: i+=1
        if ban == True:
            return (i+1)
        else:
            return False

    def MuestraTityAnio(self,ind):
        print('LIBRO')
        print(self.__listaLibros[ind].getTitulo())
        print('Autor')
        print(self.__listaLibros[ind].getAutor())
        input("")
        os.system('cls')
        gc.collect()