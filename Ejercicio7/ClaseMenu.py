from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocInv import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDecodif import ObjectEncoder
import os
import time
class Menu:
    __switcher = None
    def  __init__ ( self ): 
        self.__switcher  = { 
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            8: self.opcion8,
            9: self.opcion9,
            0: self.salir
        }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , personal ):
        func = self . __switcher.get(op, lambda:print ( "Opción no válida" ))
        func (personal)

    def salir ( self,personal):
        os.system('cls')
        print ( 'Cerrando sistema... Por favor espere.' )
        time.sleep(1)
        os.system('cls')
    
    def opcion1(self,personal):
        os.system('cls')
        pos=input("Ingrese la posicion a insertar (Distinto de 0): ")
        try:
            pos=int(pos)
            if(pos==0 or pos>int(personal.getTope())):
                raise IndexError
            agente=input("Docente ---> (D)\nInvestigador ---> (I)\nPersonal de apoyo ---> (P)\nDocente Investigador ---> (DI) \nOpcion: ")
            agente=agente.lower()
            os.system('cls')
            if(agente=='d'):        #Carga de datos Docentes
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")
                docente=Docente(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra)
                personal.InsertarAgente(pos,docente)
                print("***Docente***")
                time.sleep(1)

            if(agente=='i'):            # Carga datos Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                inves=Investigador(cuil,apellido,nombre,sueldobasico,antig,areainv,tipoinv)
                personal.InsertarAgente(pos,inves)

            if(agente=='p'):            # Carga datos Personal de apoyo
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                categ=input("Categoria: ")
                pers=PersonalApoyo(cuil,apellido,nombre,sueldobasico,antig,categ)
                personal.InsertarAgente(pos,pers)

            if(agente=='di'):            # Carga datos Docente Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                
                catincent=input("Categoria en el prog. de Incentivos (I, II, III, IV o V): ")
                impextra=float(input("Importe Extra: "))

                pers=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra,areainv,tipoinv,catincent,impextra)
                personal.InsertarAgente(pos,pers)

        except ValueError:
            print("Debe ingresar un valor numerico. ")
            time.sleep(1)
        except IndexError:
            print("No es posible insertar en esta posicion. ")
            time.sleep(1)


    def opcion2(self,personal):
        try:
            agente=input("Docente ---> (D)\nInvestigador ---> (I)\nPersonal de apoyo ---> (P)\nDocente Investigador ---> (DI) \nOpcion: ")
            agente=agente.lower()
            os.system('cls')
            if(agente=='d'):                 #Carga de datos Docentes
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")
                docente=Docente(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra)
                personal.AgregarAgente(docente)
                print("***Docente***")
                time.sleep(1)

            if(agente=='i'):                     # Carga datos Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                inves=Investigador(cuil,apellido,nombre,sueldobasico,antig,areainv,tipoinv)
                personal.AgregarAgente(inves)

            if(agente=='p'):            # Carga datos Personal de apoyo
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                categ=input("Categoria: ")
                pers=PersonalApoyo(cuil,apellido,nombre,sueldobasico,antig,categ)
                personal.AgregarAgente(pers)

            if(agente=='di'):                    # Carga datos Docente Investigador
                cuil=input("Cuil: ")
                apellido=input("Apellido: ")
                nombre=input("Nombre: ")
                sueldobasico=float(input("Sueldo Básico: "))
                antig=int(input("Antiguedad: "))

                carrera=input("Carrera: ")
                cargo=input("Cargo: ")
                catedra=input("Cátedra: ")

                areainv=input("Area de Investigacion: ")
                tipoinv=input("Tipo de investigacion: ")
                
                catincent=input("Categoria en el prog. de Incentivos : ")
                impextra=float(input("Importe Extra: "))

                pers=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antig,carrera,cargo,catedra,areainv,tipoinv,catincent,impextra)
                personal.AgregarAgente(pers)

        except ValueError:
            print("Debe ingresar un valor numerico. ")

    def opcion3(self,personal):
        pos=int(input("Posicion: "))
        personal.Inciso3(pos-1)
        time.sleep(2)

    def opcion4(self,personal):
        carrera=input("Carrera: ")
        carrera=carrera.lower()
        personal.ListadoPorNombre(carrera)
        input("Pulse ENTER para continuar...")

    def opcion5(self,personal):
        os.system('cls')
        area=input("Ingrese el area de investigacion: ")
        area=area.lower()
        personal.inciso5(area)
        input("")

    def opcion6(self,personal):
        personal.OrdenaPorApellidos()
        for p in personal:
            print("*** Datos ***")
            print("Nombre: {}".format(p.getNombre()))
            print("Apellido: {}".format(p.getApellido()))
            print("Tipo de agente: {}".format(p.__class__.__name__))
            print("Sueldo: {}".format(p.getSueldo()))
        input("")

    def opcion7(self,personal):
        cat=input("Ingrese categoria (I, II, III, IV o V): ")
        personal.BuscaPorCategorias(cat)
        input("")
    def opcion8(self,ve):
        Nuevo=ve.toJson()
        Json=ObjectEncoder()
        Json.GuardarArchivo(Nuevo,('Personas Agentes.json'))
        os.system('cls')
        print("*** ARCHIVO GUARDADO ***")
        time.sleep(1)


    
    def opcion9(self,per):
        per.mostrar()
        input("")