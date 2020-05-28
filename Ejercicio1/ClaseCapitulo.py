class Capitulo:
    __titulo = ""
    __cantidadPaginas = 0

    def __init__(self,titulo,paginas):
        self.__titulo=titulo
        self.__cantidadPaginas=paginas

    def getTitulo(self):
        return self.__titulo
    def getPaginas(self):
        return int(self.__cantidadPaginas)