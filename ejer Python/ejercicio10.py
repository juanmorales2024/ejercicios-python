minutosDia1=int(input("ingrese la cantidad de minutos del primer dia"))
minutosDia2=int(input("ingrese la cantidad de minutos del segundo dia"))
minutosDia3=int(input("ingrese la cantidad de minutos tercer dia"))

#distancia recorrida de los tres dias de entrenamiento'''
distanciaDia1=int(input("ingrese la distancia recorrida del primer dia en metros"))
distanciaDia2=int(input("ingrese la distancia recorrida del segundo dia en metros"))
distanciaDia3=int(input("ingrese la distancia recorrida del tercer dia en metros"))

#tiempo total y distancia total durante los tres dias'''
numeroDias=3
minutosTotal=minutosDia1+minutosDia2+minutosDia3
distanciaTotal=distanciaDia1+distanciaDia2+distanciaDia3

#promedio del tiempo y distancia recorrida durante los tres dias'''
promedioTiempo=minutosTotal//numeroDias
promedioDistancia=distanciaTotal//numeroDias

#resultados de los calculos'''
print(f"la cantidad de minutos durante los tres dias fue de, {minutosTotal}")
print(f"la diatancia recorrida durante los tres dias fue de, {distanciaTotal}")
print(f"el promedio del tiempo durante los tres dias fue de, {promedioTiempo}")
print(f"el promedio de la distancia recorrida en los tres dias fue de, {promedioDistancia}")
