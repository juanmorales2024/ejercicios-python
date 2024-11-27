numero1 = int(input("ingrese el pimer numero:"))
numero2 = int(input("ingrese el segundo numero:"))
numero3 = int(input("ingrese el tercero numero:"))
numero4 = int(input("ingrese el cuarto numero:"))
if numero1>numero2:
    print("el numero mayor es ",numero1)
elif numero2>numero3:
    print("el numero mayor es ",numero2)
elif numero3>numero4:
    print("el numero mayor es ",numero3)
elif numero4>numero2:
    print("el numero mayor es ",numero4)
else:
    print("todos los numeros son iguales")
