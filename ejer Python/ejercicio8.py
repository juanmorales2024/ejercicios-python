# Definir el costo de las llamadas para cada operador
costo_llamada_operador_1=int(input("ingrese el costo de la llamada"))
costo_llamada_operador_2=int(input("ingrese el costo de la llamada"))

# Definir el número de llamadas a cada operador
numero_llamadas_operador_1=2
numero_llamadas_operador_2=2

# Calcular el costo de cada llamada
costo_total_operador_1 = numero_llamadas_operador_1 * costo_llamada_operador_1
costo_total_operador_2 = numero_llamadas_operador_2 * costo_llamada_operador_2

# Calcular el costo total de las 4 llamadas
costo_total_general = costo_total_operador_1 + costo_total_operador_2

# Mostrar los resultados
print(f"Costo de cada llamada al operador 1: ${costo_llamada_operador_1}")
print(f"Costo de cada llamada al operador 2: ${costo_llamada_operador_2}")
print(f"Costo total de las llamadas al operador 1: ${costo_total_operador_1}")
print(f"Costo total de las llamadas al operador 2: ${costo_total_operador_2}")
print(f"Costo total de las 4 llamadas: ${costo_total_general}")
