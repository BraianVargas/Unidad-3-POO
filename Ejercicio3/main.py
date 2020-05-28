from ManejadorTaller import ManejaTaller
from ManejadorInscripciones import ManejaIns
from ManejadorPersonas import ManejaPersona
from Menu import Menu
import os
if __name__ == '__main__':
   
   MT=ManejaTaller()
   MI=ManejaIns()
   MP=ManejaPersona()
   menu = Menu()
   salir = False
   while not salir:
      os.system('cls')
      print("\n------------Menu------------")
      print("1. cargar archivo talleres")
      print("2. Inscribir una persona")
      print("3. buscar inscripto por Dni")
      print("4. Taller para conocer inscriptos")
      print("5. Registrar pago")
      print("6. Guardar archivo")
      print("0. Salir")
      op = int(input('Ingrese una opcion: '))
      os.system('cls')
      menu.opcion(op,MT,MI,MP)
      salir = op == 0