def bisiesto_si_o_no(anio):
    try:
        anio = int(anio)
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print()
            print("es bisiesto")
            print()
            print("Programa terminado")
        else:
            print()
            print("no es bisiesto")
            print()
            print("Programa terminado")
    except ValueError:
        print("Solo numeros, por favor reinicia el programa")
    except Exception as e:
        print(f"Ops.... Ocurrio un error no esperado: {e}")

bisiesto_si_o_no(input("Ingresa un numero: "))