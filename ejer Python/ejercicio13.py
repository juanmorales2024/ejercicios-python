# Solicitar el área total del terreno al usuario
areaTotal = float(input("Ingrese el área total del terreno en metros cuadrados: "))

# Porcentajes de cada destino
porcentajeCultivos = 40
porcentajeVivienda = 25
porcentajeZonasVerdes = 15

# Cálculo de las áreas para cada destino
areaCultivos = (porcentajeCultivos / 100) * areaTotal
areaVivienda = (porcentajeVivienda / 100) * areaTotal
areaZonasVerdes = (porcentajeZonasVerdes / 100) * areaTotal

# Cálculo del área restante
areaRestante = areaTotal - (areaCultivos + areaVivienda + areaZonasVerdes)

# Imprimir los resultados
print(f"Área destinada para cultivos: {areaCultivos:.2f} m²")
print(f"Área destinada para vivienda: {areaVivienda:.2f} m²")
print(f"Área destinada para zonas verdes: {areaZonasVerdes:.2f} m²")
print(f"Área disponible para otros proyectos: {areaRestante:.2f} m²")