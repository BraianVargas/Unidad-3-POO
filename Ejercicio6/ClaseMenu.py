from ClaseUsado import Usado
from ClaseNuevo import Nuevo
from ClaseDecodificador import ObjectEnconder
import os
import time
class Menu:
    __switcher = None
    def  __init__ ( self ): 
        self.__switcher  = { 
            1: self.opcion1 ,
            2: self. opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            0: self.salir
        }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , vehiculos ):
        func = self . __switcher . get ( op , lambda:print ( "Opción no válida" ))
        func ( vehiculos )
    def salir ( self,vehiculos):
        os.system('cls')
        print ( 'Cerrando sistema...' )
        time.sleep(1)
    def opcion1(self,vehiculos):
        os.system('cls')
        posicion=input("Ingrese la posicion a insertar: (Distinto de 0)")
        try:
            posicion=int(posicion)
            vehiculo=input("Usado(U) o Nuevo(N) --> ")
            if (vehiculo.lower()=='u'):
                modelo=input("Modelo: ")
                puertas=int(input("Cantidad de puertas. "))
                col=input("Color: ")
                base=int(input("Precio base: "))
                marca=input("Marca: ")
                pat=input("Patente: ")
                año=int(input("Año: "))
                km=int(input("Kilometraje: "))
                vehic=Usado(modelo,puertas,col,base,marca,pat,año,km)
                vehiculos.InsertarVehiculo(posicion-1,vehic)
            if (vehiculo.lower()=='n'):
                modelo=input("Modelo: ")
                puertas=int(input("Cantidad de puertas. "))
                col=input("Color: ")
                base=int(input("Precio base: "))
                version=input("Version: ")
                ve=Nuevo(modelo,puertas,col,base,version)
                vehiculos.InsertarVehiculo(posicion-1,ve)
        except ValueError:
            print("Debe ingresar un numero entero...")
            time.sleep(1)

    def opcion2(self, vehiculos):
        os.system('cls')
        vehiculo=input("Usado(U) o Nuevo(N) --> ")
        if (vehiculo.lower()=='u'):
            modelo=input("Modelo: ")
            puertas=int(input("Cantidad de puertas. "))
            col=input("Color: ")
            base=int(input("Precio base: "))
            marca=input("Marca: ")
            pat=input("Patente: ")
            año=int(input("Año: "))
            km=int(input("Kilometraje: "))
            vehic=Usado(modelo,puertas,col,base,marca,pat,año,km)
            vehiculos.AgregarVehiculo(vehic)
        if (vehiculo.lower()=='n'):
            modelo=input("Modelo: ")
            puertas=int(input("Cantidad de puertas. "))
            col=input("Color: ")
            base=int(input("Precio base: "))
            version=input("Version: ")
            vehic=Nuevo(modelo,puertas,col,base,version)
            vehiculos.AgregarVehiculo(vehic)

    def opcion3(self,vehiculos):
        os.system('cls')
        pos=input("Posicion: ")
        try:
            pos=int(pos)
            vehi=vehiculos.MostrarVehiculo(pos-1)
            if(vehi!=None):
                print("{}".format(vehi))
                time.sleep(1)
        except ValueError:
            print("Debe ingresar un numero entero...")
            time.sleep(1)

    def opcion4(self,vehiculos):
        os.system('cls')
        pat=input('Patente ')
        vehic=vehiculos.ModificaBase(pat)
        if(vehic!=0):
            print('Precio Venta {}'.format(vehic.CalcPrecioVenta()))
            time.sleep(1)
        else:
            print('Patente incorrecta')
            time.sleep(1)

    def opcion5(self, vehiculos):
        os.system('cls')
        ve=vehiculos.Minimo()
        print("***Precio del vehiculo mas economico. ***")
        print("$ {}".format(ve.CalcPrecioVenta()))
        print(ve)
        time.sleep(5)

    def opcion6(self, vehiculos):
        os.system('cls')
        vehiculos.Mostrar()
        input("")
    def opcion7(self,ve):
        os.system('cls')
        Nuevo=ve.toJson()
        Json=ObjectEnconder()
        Json.GuardarArchivo(Nuevo,('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 3/2020/Practica/Ejercicio 6/vehiculos2.json'))
        print("*** ARCHIVO GUARDADO ***")
        time.sleep(1)