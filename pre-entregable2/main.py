from my_app.clase_usuario import Usuario

cliente = Usuario("Daniel", 32, "danielitogomez@gmail.com")


print()
print(cliente.__str__())
print()
cliente.presentarse()
print()
cliente.online()
print()
cliente.offline()