from ClaseMenu import Menu

from ClasManejador import ManejaLibro

import csv

import os

if __name__ == '__main__':
    libros = ManejaLibro()
    libros.cargaLibros()
    

    menu = Menu()
    salir = False
    while not salir:
        os.system('cls')
        print("\n------------Menu------------\n1. Buscar Libro por ID\n2. Buscar libro por palabra\n3. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op, libros)
        salir = op == 3
    print(salir)