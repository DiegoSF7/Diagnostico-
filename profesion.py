class Profesion:
    def __init__(self,nombre,sueldo,cantidad):
        self.__nombre = nombre
        self.__sueldo = sueldo
        self.__cantidad = cantidad



    def setNombre(self,nombre):
        self.__nombre = nombre

    def setSueldo(self,sueldo):
        self.__sueldo = sueldo


    def setCantidad(self,cantidad):
        self.__cantidad = cantidad


    def getNombre(self):
        return self.__nombre
    
    def getCantidad(self):
        return self.__cantidad
    
    def getSueldo(self):
        return self.__sueldo
    



ingenieros = Profesion("Ingenieria",0,0)
abogados = Profesion("Abogacia",0,0)
otros = Profesion("Otros",0,0)

