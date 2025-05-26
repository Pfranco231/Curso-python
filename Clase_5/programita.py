preguntar_nombre = input("Tu nombre: ").capitalize()
preguntar_edad = int(input("Tu edad: "))
preguntar_lugar = input("Donde Vivis: ").capitalize()

def presentacion_de_persona(nombre, lugar, edad):
    print(f"Hola mi nombre es: {nombre}, tengo: {edad} Años, Vivo en: {lugar}")
    
presentacion_de_persona(preguntar_nombre, preguntar_lugar, preguntar_edad)


# Otro Programita

mi_lista = [
 1,2,3,4
]


print(mi_lista)



# Esta funcion va a modicar la variable global

#para comparar type no hace falta poner todo lo que muestra por consola si no con poner int o float
#es suficiente
def agregar(lista, numero):
    if type(numero) == int or type(numero) == float:
        lista.append(numero)
        print(f"lista modificada {lista}" )
    else:
        print("No valido")
        
    
agregar(mi_lista, 2.0)