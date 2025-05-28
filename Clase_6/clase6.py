
#Probando TRY y EXCEPT y abajo FINALLY el manejo de errores bonitos 
#Nota: se puede poner varios except como quieras es como el elif


def bisiesto_si_o_no(anio):
    #Hacemos un try que significa que va a intentar probar un pedacito de codigo 
    try:
        anio = int(anio)
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print()
            print("es bisiesto")
            print()
            print("Programa terminado")
        else:
            print()
            print("no es bisiesto")
            print()
            print("Programa terminado")
    # Agarramos el error de tipo de valor antes de que pase y imprimimos algo para el usuario
    except ValueError:
        print("Solo numeros, por favor reinicia el programa")

    # La de exception as e significa que la Exception(Error) se almacena en una variable por lo general E
    # la exception representa a cualquier error inesperado no especificado anteriormente como un metodo de seguridad
    except Exception as e:
        print(f"Ops.... Ocurrio un error no esperado: {e}")

bisiesto_si_o_no(input("Ingresa un numero: "))




#Ok sigamos con finally
# Las """  """ son tambien comentarios pero es como que estan en el codigos pero no funcionan

""" Finally: """ #Esto significa (dentro del bloque "Try")
"""     print("me Estoy ejecuntando siempre") """#que por mas que no haya una excepcion o si va a ejecutar un bloque final
                 #por eso se llama Finally 

# Puede servir para cuando cusimos recursos por input, abrir archivos, apis etc 
# Tenemos que liberar al final por eso para ahorrar memoria

#podes acumular varios exceptiones en except como asi

"""except (ValueError, ZeroDivisionError):"""
"""     print("hay un error")"""


#Raise sirve para forzar una excepcion para hacerla tu mismo

#Es diseñado para romper el codigo para testear y probar capas

"""Raise ValueError:"""
""" print("ey ey pequeña que tu aqui haces")  """




##Clases en python
##Clases en python
##Clases en python
##Clases en python
##Clases en python

#Es para crear plantillas para crear objetos como la clase de persona pero sin hacer tantas funciones personas
# es para crear una plantillas para poder crear mas

class Persona:
    #__init__: esta difiendo la funcion constructura(los actributos)
    #self: define las propiedas (en este caso el nombre y edad, como el this en js)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #estos son metodos (como atributo en la funcion siempre self)
    def saludar(self):
        #Aca usandolos 
        print(f"Hola soy {self.nombre} y tengo {self.edad} años ")
        
        
    #__str__: returna un string como en una funcion comun
    def __str__(self):
        return f"Persona: {self.nombre} {self.edad}"


#Aca creamos una persona con las plantillas y definiedoles el nombre y edad

primer_persona = Persona("Jaun", 28)
print(primer_persona)

#Primer persona nombre: 
print(primer_persona.nombre)

#Por edad:
print(primer_persona.edad)

#ejecutar un metodo:
primer_persona.saludar()
