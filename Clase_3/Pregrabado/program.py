print(":) Programa para calcular nota final Estudiantes")
nota_1 = int(input("Primera Nota: "))
nota_2 = int(input("Segunda Nota: "))
nota_3 = int(input("Tercera Nota: "))



#NOTA MUY IMPORTANTE EN PYTHON NO EXISTE EL |, & Y ESO COMO EN JS # EN PYTHON SE USA AND Y OR Y DEMAS 
if nota_1 <= 10 and nota_2 <= 10 and nota_3 <= 10:
    suma = nota_1 + nota_2 + nota_3

    dividir_entero = suma // 3 
    dividir = suma / 3

    print(f"El resultado del promedio de la nota final es: {dividir}(nota con decimal), {dividir_entero}(nota redondeada)")

    print("--------------------------------------------------------------------------")
else:
    print("No se puede poner nota mas alta que 10")
    
