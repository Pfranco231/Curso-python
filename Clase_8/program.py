#pregunta = input("Que quieres escribir: ")


""" #Open significa que va a abrir el archivo "direccion-del-archivo.extension"
#la W significa Write 
# R == read
# W == write
# A == append
archivo = open("archivo-clase.txt", "w")
#Funcion integrada en este caso queremos escribir
archivo.write(pregunta)
archivo.close() """

""" archivo = open("archivo-clase.txt", "a")
#Funcion integrada en este caso queremos escribir
archivo.write(f"\n {pregunta}")
archivo.close() """

""" archivo2 = open("archivo-clase.txt", "r")
print()
print("Resultado Final:")
print()
#hay que guardarlo en una variable
contenido = archivo2.read()
print(contenido)
archivo2.close() """


###################################################################################

print()
with open("archivo-clase.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("archivo-clase.txt", "a") as archivo2:
    contenido2 = archivo2.write("\nHola mi gente estoy en un video")
    print(contenido2)
print()


