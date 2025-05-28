
# Aqui le damos los variables 
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el primer numero: "))


# Utilizando la funcion con parametros 
def sumar(a, b):
    resultados = a + b
    #Aqui retornamos
    return resultados
    


sumar(numero1, numero2)



#Al ser un lenguaje que va linea por linea no se puede hacer esto
#
#funcion()
#def funcion():
#
#Eso da error 
print()
 
# y si son los dos paramtros obligatoriamente por que si no funciona se queda pillados(Da error)
#tambien podemos utilizarlo asignarlo por nombre (Para mi queda mejor)
resultado_final = sumar(a=numero1, b=numero2)

print(resultado_final)

#Ahora entiendo mejor el return osea basicamente por ejemplo queremos que devuelva el resultado
# de un operacion matematica muy complicada en vez de hacer directo un print o algo en la funcion
# hacemos un return resultado para que devuelva ese resultado y despues lo podemos usar para otra cosa


#Siempre bien definidos las funciones para evitar confuciones y para ahorrar tiempo
#y si es un nombre largo y se separa con _ como hola_gente_ayuda nunca abreviado
def saludo():
   print("Hola gente")
   
   
#el scope global y local igualito a js:

# este es scope global que se puede acceder desde cualquier lugar
variable2 = 5
def sumar():
    # este scope local solo se puede acceder desde la funcion
    variable = 2

#para terminar la funcion obligamente es pass y que lo pase por mas que no haya codigo
def cualquier_funcion():
    pass

""" O tambien sirve el ..."""

   
cualquier_funcion()

#Hacemos mas cosas