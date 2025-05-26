Verdadero = True
Falso = False

print(f"v: {Verdadero}, f:{Falso}")

print(10 < 3)

# Comparacion de str ??????

## print("hola" == "hola")
## print("hola" > "ho")
## print("hola" < "ho")
## print("hol" <= "hola")
## print("hol" >= "hola")



# Super Curioso

# AND, OR, NOT
a = True
b = True
c = True

print(a and b and c)
print()
print()

a = True
b = False
c = True

print(a and b and c)
print()
print()

# OR

h = True
f = False

print(h or f)
print()

h = False
f = False

print(h or f)


# Not true (basicamente dar vuelta los roles) (negar el resultado de una opcion booleana)

a = True
b = False
print()
print("Not, Dar Vueltas los roles")
print(f"verdad: {not a}, falso: {not b}")


# IF PAPA LA MEJOR MI AMIGA, ESPOSA(POR AHORA), MI NOVIA es con parentensis(buena practica) si no solo

numero1 = int(input("numero pa >>> "))

if (numero1 > 10):
    print("____________________Sos un capo capo___________________")
    
elif (numero1 < 10):
    print("Sos otro capo")
    
elif (numero1 < -1):
    print("numeros negativos????")
    
else:
    print("10 solo por dios")
