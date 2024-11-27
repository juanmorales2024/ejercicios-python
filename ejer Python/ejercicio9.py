#algoritmo para calcular el area del baño y saber cuantas baldosas debe colocar'''
altura=int(input("ingrese la altura del baño"))
largo=int(input("ingrese el largo del baño"))
baldosasTotal=3.5
areaTotal=altura*largo
totalBaldosas=areaTotal*baldosasTotal
print(f"el area del baño es: {areaTotal}")
print(f"el numero de baldosas a utilizar es: {totalBaldosas}")
