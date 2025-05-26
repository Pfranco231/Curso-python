# preguntar_al_usuario = int(input('Elegi un año(2018, 2014, 2010, 2006): '))


campeones = {
  2018 : 'Francia',
  2014 : 'Alemania',
  2010 : 'España',
  2006 : 'italia'
}


# print(campeones[preguntar_al_usuario])

# Desafio de la clase anterior


#esto es una lista con dentro deccionarios
personas = [
    {
        "nombre": "Carlos",
        "apellido": "Ramírez",
        "edad": 20,
        "curso": "Matemáticas"
    },
    {
        "nombre": "Lucía",
        "apellido": "Gómez",
        "edad": 22,
        "curso": "Biología"
    },
    {
        "nombre": "Andrés",
        "apellido": "Martínez",
        "edad": 19,
        "curso": "Historia"
    },
    {
        "nombre": "Sofía",
        "apellido": "López",
        "edad": 21,
        "curso": "Física"
    }
]




#Asi se hace para buscar las personas por clave
print(personas[0].keys())


#Asi se hace para buscar las personas por valor
print(personas[0].values())

#clear all
personas.clear()
print(personas)