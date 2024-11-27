numeroInicio=int(input("Ingrese el numero con que inicio el dia:"))
numeroFin=int(input("ingresa el numero con el que termino el dia:"))
cantidadPasajeros=numeroInicio+numeroFin
print(f"la cantidad de pasajeros es {cantidadPasajeros}")
costoPasaje=float(input("Ingrese el costo del pasaje:"))
gananciaEmpresa = costoPasaje * 0.75
gananciaConductor = costoPasaje * 0.25
print(f"la ganancia del conductor es de:  {gananciaConductor}")
print(f"la ganancia de la empresa es de:  {gananciaEmpresa}")