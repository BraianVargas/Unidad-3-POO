from ClaseEmpleados import Empleados
from ClaseColeccion import Coleccion
from ClasePlanta import Planta
from ClaseContratados import Contratados
from ClaseExternos import Externos
from Menu import Menu
import csv
import time
import os

if __name__=='__main__':
    ban=False
    while(ban==False):
        os.system('cls')
        cant=input("Ingrese la cantidad de empleados ")
        cant=int(cant)
        colec=Coleccion(cant)
        if(colec.CargarEmpleados()!=-1):
           ban=True 
    
    menu = Menu()

    salir = False
    while not salir:
        os.system('cls')
        print("1. Registrar Horas")
        print("2. Mostrar Total a Pagar por Tarea")
        print("3. Registrar ayuda solidaria")
        print("4. Calcular Sueldo")
        print("5. Ingresar como Tesorero.")
        print("6. Ingresar como Gerente")
        print("0. Salir")
        print("")
        op = input('Ingrese una opcion: ')
        try:
            op=int(op)
            menu.opcion(op,colec)
            salir = op == 0
        except ValueError:
            print("Ingrese un numero de opción.")
            time.sleep(0.5)