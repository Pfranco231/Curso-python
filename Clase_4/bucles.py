# Bucles(no son muy buenas pero las voy a dominar)


listita = [1,2,3,"hola", 5,6,7]

print(f"Print Comun: {listita[3]}")


# ITERAR LA LISTA
# i = es una variable(donde se guarda todo), listita = es la lista de datos (es el donde itera)
# Aca es diferente como esta difenido tiene un final no como el while
# for i in listita:
#     print(i)


# i = variable
i = 0

# es menor que la cantidad de la listita(uso len para ver la lengitud)
# hay que indicarle cuando parar en este caso cuando sea igual que el len de la lista
while i < len(listita):
    # imprime la lista
    print(f"Valor: {listita[i]}, Valor I: {i}")
    # aumenta el i para que no sea un bucle infinito
    i += 1
    
    
def funcion(a, b):
    resultado = a + b
    return resultado



resultado_final = funcion(5, 6)
print(resultado_final)
# En que casos podria servir el while true(osea infinito)
# Una mini calculadora donde siempre se ejecuta ejecuta y asi
# y cuando queres salir hace un break

# Actividad practica: para mi(crear una calculadora) con while true(bucle infinito siempre true) y break(para salir del bucle)
# O hacer un preguntados basicos con temas