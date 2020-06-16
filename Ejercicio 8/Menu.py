import os
import time
import csv
import sys

class Menu:
    __userT="uTesorero"
    __passwT="ag@74ck"
    __userG="uGerente"
    __passwG="ufC77#!1"

    
    __switcher = None
    def  __init__ (self):
        self.__switcher  = {1:self.opcion1 ,
                            2:self.opcion2 ,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            0:self.salir
                         }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op, colec):
        func = self . __switcher . get ( op , lambda:print( "Opción no válida" ))
        func (colec)
        time.sleep(.6)

    def salir(self,colec):
        print('Cerrando sistema...')
        time.sleep(1)

    def opcion1(self,colec):
        dni=input("Ingrese el DNI del empleado: ")
        try:
            dni=int(dni)
            empl=colec.BuscarDNI(dni)
            if((empl!=0) and (empl!=-1)):
                horas=int(input("Ingrese cantidad de horas: "))
                try:
                    nuevo= horas + empl.getHoras()
                    empl.setHoras(nuevo)
                    ban=True
                    if(ban==True):
                        os.system('cls')
                        print("Horas Registradas.")
                        print("Cantidad total de horas: {}" .format(empl.getHoras()))
                        print("Empleado: {}".format(empl.getNom()))
                        input("")
                except:
                        print("No se ha podido registrar horas.")
                        print("Es posible que el empleado no trabaje por horas.")
                        input("")
            else:
                if(empl==-1):
                    print("ERROR! Es posible que el empleado no esté registrado o no trabaje por horas")
                    input("")
                else:
                    print("EMPLEADO NO ENCONTRADO!")
                    input("")
        except ValueError:
            print("Debe ingresar un dni valido")
            input("")

    def opcion2(self,colec):
        os.system('cls')
        tarea=input("Ingrese tarea: ")
        tarea=tarea.lower()
        colec.BuscarTarea(tarea)
        

    def opcion3(self,colec):
        colec.AyudaSolid()

    def opcion4(self,colec):
        os.system('cls')
        colec.MuestraSueldos()
        time.sleep(1)


    def opcion5(self,colec):
        ban=False
        while(ban==False):
            us=input("Usuario: ")
            ps=input("Contraseña: ")
            if(us==self.__userT and ps==self.__passwT):
                ban=True
                dni=input("Ingrese DNI: ")
                try:
                    dni=int(dni)
                    colec.gastosSueldoPorEmpleado(dni)
                except ValueError:
                    print("Debe ingresar un valor Numerico.")
                    time.sleep(1)
            else:
                print("Usuario o contraseña incorrecto. Intente nuevamente.")
                time.sleep(1)
            input("Presione ENTER para continuar.")

    def opcion6(self,colec):
        os.system('cls')
        ban=False
        while(ban==False):
            us=input("Usuario: ")
            ps=input("Contraseña: ")
            if(us==self.__userG and ps==self.__passwG):
                ban=True
                dni=input("Ingrese el DNI: ")
                try:
                    dni=int(dni)
                    print("1. Modificar Basico E. Planta")
                    print("2. Modificar Viatico E. Externo")
                    print("3. Modificar Valor E. Por Hora")
                    print("0. Menu principal. ")
                    op=int(input("Ingrese su opcion: "))
                    while(op!=0):
                        if(op==1):
                            os.system('cls')
                            nuevo=int(input("Ingrese el nuevo valor del básico: "))
                            colec.modificarBasicoEPlanta(dni,nuevo)
                            input("Presione ENTER para continuar.")
                        if(op==2):
                            os.system('cls')
                            nuevo=int(input("Ingrese el nuevo valor del Viatico: "))
                            colec.modificarViaticoEExterno(dni,nuevo)
                            input("Presione ENTER para continuar.")
                        if(op==3):
                            os.system('cls')
                            nuevo=int(input("Ingrese el nuevo valor de hora: "))
                            colec.modificarValorEPorHora(dni,nuevo)
                            input("Presione ENTER para continuar.")

                        print("1. Modificar Basico E. Planta")
                        print("2. Modificar Viatico E. Externo")
                        print("3. Modificar Valor E. Por Hora")
                        print("0. Menu principal. ")
                        op=int(input("Ingrese su opcion: "))
                        
                except ValueError:
                    os.system('cls')
                    print("Debe ingresar un valor Numerico.")
                    time.sleep(1)
            else:
                print("Usuario o contraseña incorrecto. Intente nuevamente.")
                time.sleep(1)
            input("Presione ENTER para continuar.")