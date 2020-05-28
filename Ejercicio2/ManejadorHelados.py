from ClaseHelado import Helado
class ManejaHelados:
    
    __listaVendidos=[]

    def __init__(self):
        self.__listaVendidos=[]

    def nuevaVenta(self,sabores):
        grs=input("Ingrese la cantidad de gramos:")
        try:
            grs=int(grs)
            hel=Helado(grs)
            
            ban=True
            while ban!=False:
                sabor=input("Ingrese el sabor (Nombre) (Finaliza con fin): ")
                sabor=sabor.lower()
                if(sabor!="fin"):
                    if(sabores.buscaSaborxNombre(sabor) == True):
                        hel.AgregaSabores(sabor)
                    else:
                        print("El sabor no está disponible. ")
                        print("Intente nuevamente con otro sabor. ")
                else:
                    self.__listaVendidos.append(hel)
                    ban=False
        except ValueError:
            print("ERROR. Debe ingresar un numero entero.")
            input("")

    def mostrarPedido(self):
        i = len(self.__listaVendidos)-1
        print("'******** PEDIDO ********")
        print("| Helado de {} Gr " .format(self.__listaVendidos[i].getGr()))
        print("|**** Sabor/es ****")
        print(self.__listaVendidos[i].verSabores())
    
    def buscaSaborporNum(self, num):
        i=0
        gramosVendidos=0
        while(i<len(self.__listaVendidos)):
            total=0
            if(int(self.__listaVendidos[i].BuscaxNumero(num)==1)):
                cant=self.__listaVendidos[i].cantGramos()
                sab=self.__listaVendidos[i].contSabores()
                total=cant/sab
                gramosVendidos=gramosVendidos+total
            i=i+1
        return gramosVendidos
