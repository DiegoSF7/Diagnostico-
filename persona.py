class Persona:
    def __init__(self,nombre,edad,genero,profesion):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        self.__profesion = profesion


    def setNombre(self,nombre):
        self.__nombre = nombre
    def setEdad(self,edad):
        self.__edad = edad
    def setGenero(self,genero):
        self.__genero = genero
    def setProfesion(self,profesion):
        self.__profesion = profesion

    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getGenero(self):
        return self.__genero
    
    def getProfesion(self):
        return self.__profesion
    


    
