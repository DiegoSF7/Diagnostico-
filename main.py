from persona import *
from profesion import *

# 1) Los pilares fundamentales de la POO constan de 4 estructuras las cuales son:
# Abastraccion: Indica la especifidad que existen en las clases y metodos que estos poseen 
# Encapsulamineto: Se trata de privatizar los atributos de una clase para asi alcanzar a tener una mejor seguridad o evitar que se modifiquen archivos por error
# Polimorfismo: el polimorfismo es una cualidad que posee la POO en el cual hace que 1 solo metodo pueda cambiar dependiendo de la clase, haciendo que existan multiples formas de usar un metodo
# Herencia: Este pilar permite crear una nueva clase, "herendado" asi los atributos de su padre y ademas agregandole los de el mismo


# 2) La mejor forma de explicar el tema de las clases es usando la palabra "molde". Una clase basicamente es el molde que se utiliza para poder crear objetos que poseen atributos en comun.
# Ej: Todos los carros poseen un color,nombre , marca, asientos etc, pero, no todos estos atributos poseen los mismos valores, es ahi donde entran los objetos


# 3) Un objeto es el resultado de haber instanciado mediante una clase, es decir, cuando usamos el "molde" para crear asi un elemento con diversas cualiades. Usando el ejemplo anterior podemos decir
# que un objeto seria un carro de color rojo, nombre viper, marca dodge y 2 asientos.
# otro


def verSueldo():
    try:
        ingSueldo = ingenieros.getSueldo() / ingenieros.getCantidad()
        aboSueldo = abogados.getSueldo() / abogados.getCantidad()
        otherSueldo = otros.getSueldo() / otros.getCantidad()
        print("-"*40)
        print("")
        print(f"Sueldo promedio de Ingenieria: ${int(ingSueldo)}")
        print(f"Sueldo promedio de Abogacía: ${int(aboSueldo)}")
        print(f"Sueldo promedio de Otros: ${int(otherSueldo)}")
        print("")
        print("-"*40)
    except:
        print("")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Todas las profesiones deben estar completas!")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("")


def verPorcentaje():
    try:
        total = ingenieros.getCantidad() + abogados.getCantidad() + otros.getCantidad()
        ingPorcentaje = ingenieros.getCantidad() / total * 100
        aboPorcentaje = abogados.getCantidad() / total * 100
        otherPorcentaje = otros.getCantidad()/ total * 100
        print("-"*40)
        print("")
        print(f"Personas en Ingenieria {ingPorcentaje}%")
        print(f"Personas en Abogacía {aboPorcentaje}%")
        print(f"Personas en Otros {otherPorcentaje}%")
        print("")
        print("-"*40)
    except:
        print("")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Error! No hay personas en la lista")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("")

def identificarPersona():
    print("")
    print("Por favor rellene los siguientes campos:")
    print("")

    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese su edad: "))
    while(edad < 0 ):
        edad = int(input("Ingrese una edad coherente: "))


    sexo = int(input("Ingrese su genero \n [0] - Masculino     [1] - Femenino\n"))
    while(sexo < 0 or sexo > 1):
        sexo = int(input("Ingrese un numero valido \n [0] - Masculino     [1] - Femenino\n "))


    profesion = int(input("Ingrese su profesion \n [0] - Ingenieria    [1] - Abogacia    [2] - Otros\n"))
    while (profesion < 0 or profesion > 2):
        profesion = int(input("Ingrese un numero valido \n [0] - Ingenieria    [1] - Abogacia    [2] - Otros\n"))
    if (profesion == 0):
        profesion = ingenieros
    elif (profesion == 1):
        profesion = abogados
    elif (profesion == 2):
        profesion = otros

    sueldo = int(input("Ingrese su sueldo: "))
    while(sueldo < 0 ):
        sueldo = int(input("Ingrese un sueldo valido: "))
    persona = Persona(nombre,edad,sexo,profesion)

    profesion.setSueldo(profesion.getSueldo() + sueldo)
    profesion.setCantidad(profesion.getCantidad() + 1) 
    print("")
    print("@@@@@@@@@@@@@@@@@@@")
    print("Agregado con exito")
    print("@@@@@@@@@@@@@@@@@@@")
    print("")


counter = 0
while (counter == 0):
    print("-"*40)
    print("")
    ask = int(input("Escoja una opción \n [1] - Ingresar Persona   [2] - Ver %  \n [3] - Ver Sueldos        [4]  - Salir \n"))

    while (int(ask) < 1 or int(ask) > 4):
        ask = int(input("Ingrese un numero valido \n [1] - Ingresar Persona   [2] - Ver %  \n [3] - Ver Sueldos        [4]  - Salir \n"))
    if (ask == 1):
        identificarPersona()
    elif (ask == 2):
        verPorcentaje()
    elif( ask == 3):
        verSueldo()
    elif( ask == 4):
        print("Hasta luego!")
        counter += 1
