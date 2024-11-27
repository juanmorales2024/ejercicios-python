aptitudMatematica = int(input("Ingrese el puntaje de la prueba aptitudMatematica: "))
lenguaje = int(input("Ingrese el puntaje de la prueba lenguaje: "))
if aptitudMatematica > lenguaje:
    print("el puntaje mayor es :",aptitudMatematica)
elif lenguaje > aptitudMatematica:
    print("el puntaje mayor es :",lenguaje)
else:
    lenguaje = aptitudMatematica
    print("ambos puntajes son iguales ")