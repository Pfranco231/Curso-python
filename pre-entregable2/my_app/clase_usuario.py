class Usuario:
    def __init__(self, nombre, edad, mail):
        self.nombre = nombre
        self.edad = edad
        self.mail = mail
    
    def __str__(self):
        return f"Nombre(self.nombre): {self.nombre}, Edad(nombre.edad): {self.edad}, Mail(self.mail): {self.mail}"
        

    def presentarse(self):
        print(f"Hola, Mi Nombre de usuario es: {self.nombre}, Tengo: {self.edad} \nMi Mail de contacto es: {self.mail}")
    
    def offline(self):
        print(f"El usuario: {self.nombre}, Actualmente esta Offline")
        
    def online(self):
        print(f"El usuario: {self.nombre}, Actualmente esta Online")