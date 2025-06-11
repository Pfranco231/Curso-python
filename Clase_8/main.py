#importar archivos nuestros 
#estamos creando codigo reutilizando

#
#Este es el mejor por que llamamos cada funcion con modulo1.(funcion o clase cualquiera)
from ejemplo_preentrega import modulo1
from ejemplo_preentrega import modulo2



#que de un archivo especifico llamamos una funcion
#Suele pisar con las funciones del main principal que si se cruzan 
"""from ejemplo_preentrega.modulo1 import hola_mundo"""
#esto para importar todo de un archivo
#EL MENOS RECOMENDADO
"""from ejemplo_preentrega.modulo1 import *"""


#tenemos que llamar al modulo junto con lo que vamos a necesitar 
modulo1.hola_mundo()

persona1 = modulo2.Persona("Franco", 16)

persona1.saludar()