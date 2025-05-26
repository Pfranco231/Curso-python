# Descripción de la actividad.
# Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
# gordon lanzó su curva&strawberry ha fallado por un pie!
# -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea
# la cabeza como disgustado… -agrega el comentarista
# Transforma el texto en:
# Gordon lanzó su curva...
# - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# - Dos pies le corrigió Troop.
# - Strawberry menea la cabeza como disgustado… -agrega el comentarista.
# Lo único prohibido es modificar directamente el texto

texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
print()
print()
print(f'Antes de los cambios: {texto}')


#Elimina la palabra indicada
texto1 = texto.split("&")
print()
print()
print(f'despues del split {texto1}')
print()
print()
texto1[0] = texto1[0] + ".."
print(texto1[0], "Despues de 3 Puntos")

#Primera letra en mayus pero para mi es mejor capitalize
texto1[0] = texto1[0][0].upper() + texto1[0][1:]

print()
print()



print(f'Despues del Upper {texto1[1]}')
#

#ponemos en mayusculas el primer caracter de cada oración 
texto1[1] = texto1[1][0].upper() + texto1[1][1:]
texto1[2] = texto1[2][0].upper() + texto1[2][1:]
texto1[3] = texto1[3][0].upper() + texto1[3][1:]

print(texto1, "Antes de toques Finales")
print(texto1, "Añadendo mas cosas:")


print()
print()
texto2 = ".\n-".join(texto1) + "."

print(texto2)
print()
print()

