input_user = int(input("Ingresa el primer nota: "))
input_user2 = int(input("Ingresa el segundo nota: "))
input_user3 = int(input("Ingresa el tercer nota: "))

def calcular_promedio(a,b,c):
    resultado = a + b + c / 3
    
    if (resultado > 10 ):
        return "Nota maxima: 10"
    elif (resultado < 10):
        return resultado
    else:
        print("Algo Salio mal")


print(calcular_promedio(input_user, input_user2, input_user3))


