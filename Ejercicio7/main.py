from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocInv import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDecodif import ObjectEncoder
from ClaseLista import ListaPersonal
from ClaseMenu import Menu
import os
import time

if __name__ == "__main__":
    personal=ListaPersonal()
    Json=ObjectEncoder()
    dic=Json.LeerArchivo('Personal.json')
    personal=Json.DecodificarDiccionario(dic)
    menu=Menu()
    ban=False
    while not ban:
        os.system('cls')
        print("1. Insertar Agente.")
        print("2. Agregar Agente.")
        print("3. Mostra tipo de agente por posicion.")
        print("4. Generar listado ordenado de datos por nombre de carrera.")
        print("5. Mostrar cantidad de agentes por area.")
        print("6. Generar listado de datos por apellido.")
        print("7. Listar datos por categorias.")
        print("8. Guardar Datos.")
        print("9. Mostrar Lista.")
        print("0. Salir")
        opcion=input("Ingrese una opcion: ")
        opcion=int(opcion)
        menu.opcion(opcion,personal)
        ban=opcion==0
