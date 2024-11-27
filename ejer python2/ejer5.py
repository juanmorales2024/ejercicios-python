nota=float(input("Ingrese su nota: "))
if nota >=4.6 and nota <= 5.0:
    print("Su nota cualitativa es EXCELENTE")
elif nota >= 3.6 and nota <4.6:
    print("Su nota cualitativa es BUENA")
elif nota >= 3.0 and nota <3.6:   
    print("Su nota cualitativa es ACEPTABLE")
elif nota >= 2.0 and nota <3.0:   
    print("Su nota cualitativa es INSUFICIENTE")
elif nota < 2.0 and nota >= 0.0:
    print("Su nota cualitativa es DEFICIENTE")
else:
    print("Su nota no se encuentra en el rango de 0.0 y 5.0 ")

