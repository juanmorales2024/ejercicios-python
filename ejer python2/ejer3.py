partido1=int(input("ingrese la cantidad de goles en el primer partido"))
partido2=int(input("ingrese la cantidad de goles en el segundo partido"))
partido3=int(input("ingrese la cantidad de goles en el tercer partido"))
partido4=int(input("ingrese la cantidad de goles en el cuarto partido"))

totalGoles= partido1 + partido2 + partido3 + partido4
if totalGoles > 10:
    #calcular el promedio'''
    promedio=totalGoles/4

#resultados de los calculos'''
    print(f"el numero de goles es de: {totalGoles}")
    print(f"el promedio de los goles durante los cuatro partidos: {promedio}")
else: 
    print("no se pide determinar el promedio")
    
