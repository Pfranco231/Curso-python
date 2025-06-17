#Definicion de Class en Python

#Definimos Clase persona con nombre
class Persona:
    #El __init__ es la funcion constructor que siempre se ejecuta ahi se define con Self(como el this) y atributos como nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    #En cada Funcion se usa el self ara acceder a los atributos
    #Esto es un metodo(una funcion) que creamos nosotros mismos
    def saludar(self):
        print(f"Hola, Mi nombre es {self.nombre} y tengo {self.edad} años")
        
    #Aca añadimos gustos
    def presentarse(self, gustos):
        print(f"Hola soy {self.nombre} y mis gustos son {gustos}")
        
    
    #Demuestra algo elegible y no muestra una informacion como <__main__.Persona object at 0x00000123ABCDEF>
    #Puede ser el nombre del objeto y sus metodos
    def __str__(self):
        return f"Personaaaaaaaaaa: {self.nombre} {self.edad}"
    


#Ya definimos a un persona(en este caso) con Nombre y Edad
franco = Persona("Franco", 16)

#Accedemos al nombre (un atributo)
print(franco.nombre)

#Accedemos al saludo (un metodo)
print(franco.saludar())
print(franco.presentarse("Programacion y juegos"))

#las instancias son los objetos