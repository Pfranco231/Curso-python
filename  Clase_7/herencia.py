

#Esta es la clase padre con sus atributos y metodos ya definidos y despues lo usamos como padre
class Animal:
    def __init__(self, nombre, edad):
        #aplicamos capsulamiento para que no se acceda publicamente
        self.nombre = nombre
        self.edad = edad
        
    #se puede hacer con las funciones basicamente ponemos __ antes del nombre 
    def comer(self):
        print(f"{self.nombre} esta Comiendo")
        
    def dormir(self):
        print(f"Esta durmiendo {self.nombre}")
    
    def hacer_sonido(self):
        print(f"Esta sonando {self.nombre}")
        
    



#Para hederar todo de una clase superior usamos nombre_de_la_clase(clase__padre)  y listo y modificamos una funcion de la funcion padre
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "gato")
    
    def hacer_sonido(self):
        print(f"{self.nombre} esta Maullando")
    
    


mi_gato = Gato("GRIESA")


#Y aca podemos ejecutar funciones que no tenia la clase gato pero las hereda de la clase Animal 
#pero podemos modificar una funcion del padre como en este caso el hacer_sonido eso se llama Polimorfismo
# aca no creo poner que no sea privada  pero la privacidad (no se hereda ) que es el name nambling que es hackear jaja pero
#no es recomdable hacerlo por que rompe todo SI ROMPE TODO EHHHH
mi_gato.comer()
mi_gato.dormir()
mi_gato.hacer_sonido()


#tambien podemos hacer herencia multiple 
# Ejemplo :
""" Class Carpintero(Animal, Volador) """
#Es lo mismo pero hereda de varios super clases o clases padres