from ManejadorSabores import ManejaSabores
from ManejadorHelados import ManejaHelados
from ClaseMenu import Menu
import os

if __name__=='__main__':
    sabores=ManejaSabores()
    sabores.CargaSabores()
    m=ManejaHelados()

    menu = Menu()
    salir = False
    while not salir:
        os.system('cls')
        print("\n------------------------Menu------------------------\n\n")
        print("1. Registrar Helado Vendido")
        print("2. Mostrar sabores mas pedidos")
        print("3. Ver total de gr. vendidos por sabor")
        print("4. opcion 4")
        print("5. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op,sabores,m)
        salir = op == 5
    print(salir)