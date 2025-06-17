class Animal:
    def __init__(self, nombre, edad, animal, raza):
        #aplicamos capsulamiento para que no se acceda publicamente
        self.nombre = nombre
        self.__edad = edad
        self.__animal = animal
        self.__raza = raza
        
    #se puede hacer con las funciones basicamente ponemos __ antes del nombre 
    def ladrar(self):
        print(f"gua gua")
        
    def presentarse(self, comida):
        print(f"Hola soy {self.nombre} y me gusta comer {comida} y tengo {self.__edad}")
        
    


rex = Animal("Rex", 5, "Perro", "Pitbull")

print(rex.nombre)

#Daa error por que esta privada
#print(rex.__edad)

print()
print(rex.ladrar())
print()
print(rex.presentarse("Galletas"))