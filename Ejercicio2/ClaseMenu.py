from ManejadorHelados import ManejaHelados
from ManejadorSabores import ManejaSabores
import os
class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.salir
                         }

    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, sabores,mane):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(sabores,mane)
    def salir(self,sabores,mane):
        print('Salir')

    def opcion1(self,sabores,manej):
        manej.nuevaVenta(sabores)
        print("Pedido: \n")
        manej.mostrarPedido()
        input("")

    def opcion2(self,sabores,manej):
        masVend=sabores.SaboresmasPedidos(sabores)
        print("******** SABORES MAS VENDIDOS ******** ")
        sabores.MuestraMasPedidos(masVend)
        input("")
    def opcion3(self,sabores,manejHel):
        numSab=input("Ingrese el numero del sabor que busca: ")
        try:
            numSab=int(numSab)
            tot=int(manejHel.buscaSaborporNum(numSab))
            print("Total de gramos vendidos. Sabor N° {} es {}" .format(numSab,tot))
        except ValueError:
            print ("Debe ingresar un valor entero")
            input("")
    
    def opcion4(self):
        pass
    