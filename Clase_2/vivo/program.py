# STR, Numeros

saludo = "Hola mundo"
primer_numero = 4

#lista

lista_1 = [1,2,3,4, "hola"]
print(lista_1)

#index
print(lista_1[0])
print(lista_1[2])
print(lista_1[1])

print(len(lista_1), "Contando ")


lista_1.append(6)
print(lista_1[2])



#ya sabemos que es el insert
lista_1.insert(0, 2)
#el count basicamente cuenta
print(lista_1.count(2), "hay 2 de 2")

#el pop eliminaba el ultimo
print(lista_1)
lista_1.pop()
print(lista_1)

#el pop eliminaba el ultimo eligiendo
lista_1.pop(4)
print(lista_1)


# Lista vacia pa
lista_1.clear()

#aclaracion las print no puede contactenar
print(lista_1, "Lista Vacia")