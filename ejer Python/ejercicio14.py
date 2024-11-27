# Solicitar las calificaciones
notaTaller1 = float(input("Ingrese la calificación del primer taller: "))
notaTaller2 = float(input("Ingrese la calificación del segundo taller: "))
notaEval1 = float(input("Ingrese la calificación de la primera evaluación: "))
notaEval2 = float(input("Ingrese la calificación de la segunda evaluación: "))
notaEval3 = float(input("Ingrese la calificación de la tercera evaluación: "))
notaTrabajoFinal = float(input("Ingrese la calificación del trabajo final: "))
notaQuiz1 = float(input("Ingrese la calificación del primer quiz: "))
notaQuiz2 = float(input("Ingrese la calificación del segundo quiz: "))
notaQuiz3 = float(input("Ingrese la calificación del tercer quiz: "))
notaQuiz4 = float(input("Ingrese la calificación del cuarto quiz: "))

# Calcular promedios
promedioTalleres = (notaTaller1 + notaTaller2) / 2
promedioEvaluaciones = (notaEval1 + notaEval2 + notaEval3) / 3
promedioQuizzes = (notaQuiz1 + notaQuiz2 + notaQuiz3 + notaQuiz4) / 4

# Calcular la nota definitiva
notaDefinitiva = (promedioTalleres * 0.15) + (promedioEvaluaciones * 0.30) + (notaTrabajoFinal * 0.30) + (promedioQuizzes * 0.25)

# Mostrar la nota definitiva
print(f"La nota definitiva del estudiante es: {notaDefinitiva:}")
