import os
class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.salir
                         }

    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, libros):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(libros)
    def salir(self):
        print('Salir')
    def opcion1(self, libros):
        band = False
        while not band:
            identif = input('Ingrese el id del libro: ')
            try:
                identif=int(identif)
                aux=libros.buscarId(identif)
                if  aux != False:
                    libros.mostrarDatos(libros.buscarId(identif) -1)
                    band = True
                else:
                    print('ERROR: ID de libro no encontrado, intente nuevamente.')
                    input("")
            except ValueError:
                print("ERROR. Debe ingresar un valor entero.")
                input("")
            os.system('cls')

    def opcion2(self, libros):
        palabra = input('Ingrese una palabra: ')
        palabra=palabra.lower()
        pal=libros.buscaPalabra(palabra)

        if(pal==False):
            print("No se ha encontrado libro con la palabra ingresada")
            input("")
        else:
            if(pal>=0):
                print(libros.MuestraTityAnio(pal-1))