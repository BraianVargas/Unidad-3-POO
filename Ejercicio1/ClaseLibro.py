from ClaseCapitulo import Capitulo

class Libro:
    __idLibro = 0
    __titulo = ""
    __autor = ""
    __editorial = ""
    __isbn = 0
    __cantidadCapitulos = 0
    __capitulo=[]

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor
    
    def getId(self):
        return self.__idLibro
        
    def __init__(self,idlib,tit,aut,edit,isbn,cantCap):
        self.__idLibro=int(idlib)
        self.__titulo=tit
        self.__autor=aut
        self.__editorial=edit
        self.__isbn=int(isbn)
        self.__cantidadCapitulos=int(cantCap)
        self.__capitulo=[]

    def AgregaCapitulo(self,capi):
        if(type(capi)==Capitulo):
            self.__capitulo.append(capi)
        else:
            print("ERROR. No se ha podido cargar el capitulo")
    
    def muestraCap(self):
        for i in range(self.__cantidadCapitulos):
            print("{}".format(self.__capitulo[i].getTitulo()))

    def getTotPag(self):
        tot=i=0
        for i in range(self.__cantidadCapitulos):
            tot+=self.__capitulo[i].getPaginas()
        return tot
    def buscaPal(self, palabra):
        ban=False
        i=j=0
        for i in range(len(self.__capitulo)):
            capi=self.__capitulo[i].getTitulo()
            lcap=capi.split()
            while (j < len(lcap)) and (ban == False):
                if(lcap[j] == palabra):
                    ban=True
                else: j+=1
            i+=1
        if ban == True:
            return (i+1)
        else:
            return False