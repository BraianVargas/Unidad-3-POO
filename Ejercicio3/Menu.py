import  os
from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
import datetime

class Menu :
    __switcher = None
    def  __init__ (self):
        self.__switcher  = { 1 : self.opcion1 ,
                            2 : self. opcion2 ,
                            3: self. opcion3,
                            4: self .opcion4,
                            5: self. opcion5,
                            6: self.opcion6,
                            0: self. salir
                         }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , MTaller,MInscrip,MPers):
        func = self . __switcher . get ( op , lambda : print ( "Opción no válida" ))
        func ( MTaller,MInscrip,MPers )
    def  salir ( self,MTaller,MInscrip,MPers):
        print ( 'Salir' )

    def  opcion1 (self, MTaller,MInscrip,MPers):   #Carga de Talleres
        MTaller.CargaTaller()
        os.system('cls')
        MTaller.Mostrar()

    def  opcion2 ( self,MTaller,MInscrip,MPers ):
        nom = input("Nombre:")
        dire = input('Direccion: ')
        dni = input('DNI: ')
        
        unaP=Persona(nom,dire,dni)
        MPers.AgregaPers(unaP)                      # Agrega una persona a la lista de personas

        tall =input("Nombre del taller al que se inscribe: ")

        band=0

        while(band==0):
            disp=MTaller.BuscaTaller(tall)
            if(disp==True):
                print('** Taller disponible **')
                tall = MTaller.getTaller(tall)
                band=1
            else:
              tall=input("** Taller no disponible **, elija otro: ")

        hoy = datetime.date.today()
        fecha=str(hoy)
        
        unaInscripcion=Inscripcion(fecha,False,unaP,tall)
        MInscrip.NuevaInsc(unaInscripcion)              # Agrega la inscripcion hecha a la lista de iscripciones
        MTaller.NuevoInscripto(tall,unaInscripcion)
        print("*** Inscripcion Exitosa ***\n")
        print(unaInscripcion)
        print(unaInscripcion.MuestraTaller())
        
        input("Presione ENTER para continuar")
        print('\n')

    def opcion3(self,MTaller,MInscrip,MPers):
        dni=input("Ingrese el DNI a buscar: ")
        persona=MPers.BuscaPersona(dni)            # Busca persona de dni ingresado
        if(persona!=-1):
            nom=MInscrip.BuscaIns(dni)          # Revisa que esté inscripto a algun taller
            if(nom!=False):
                MTaller.BuscaxNom(nom)
        else:
            print("No se encuentra inscripto")
        input("")

    def opcion4(self,MTaller,MInscrip,MPers):
      iden=int(input('Id Taller: '))
      MTaller.VerInscriptos(iden)

    def opcion5 (self,MTaller,MInscrip,MPers):
        dni=input('DNI de la persona')
        persona=int(MPers.BuscaPersona(dni))
        if(persona!=-1):
           MInscrip.RegistraPago(persona)
        else:
            print('No se encontro persona')
        print('-------inscripciones---')
        MInscrip.Mostrar()
        input("Presione ENTER para continuar")


    def opcion6(self,MTaller,MInscrip,MPers):
        MInscrip.GeneraArchivo()
        input("Presione ENTER para continuar")