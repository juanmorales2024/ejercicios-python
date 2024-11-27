#algoritmo para calcular el porcentaje de una herencia'''
montoTotal=float(input("ingrese el monto total de la herencia"))

#porcentajes del testamento'''
porcentajeEsposa=40
porcentajeHijo1=30
porcentajeHijo2=20
porcentajeHijo3=40
porcentajeHijo4=10

#calcular las cantidades'''
cantidadEsposa=(porcentajeEsposa/100)*montoTotal
cantidadHijo1=(porcentajeHijo1/100)*montoTotal
cantidadHijo2=(porcentajeHijo2/100)*montoTotal
cantidadHijo3=(porcentajeHijo3/100)*montoTotal
cantidadHijo4=(porcentajeHijo4/100)*montoTotal

#resultados de los calculos'''
print(f"la cantidad de la herencia para la esposa es de: {cantidadEsposa}")
print(f"la cantidad de la herencia para el hijo1 es de: {cantidadHijo1}")
print(f"la cantidad de la herencia para el hijo2 es de: {cantidadHijo2}")
print(f"la cantidad de la herencia para el hijo3 es de: {cantidadHijo3}")
print(f"la cantidad de la herencia para el hijo4 es de: {cantidadHijo4}")

