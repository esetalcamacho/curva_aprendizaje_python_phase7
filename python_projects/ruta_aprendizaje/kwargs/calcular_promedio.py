def calcular_promedio(**notas):
    if len(notas) == 0:
        return 0
    promedios = {} # Diccionario donde se almacenaran los promedios
    for asignatura, calificaciones in notas.items():
        suma_total = sum(calificaciones)  # Inicializando suma_total
        promedio = suma_total / len(calificaciones)  # Inicializando promedio
        promedios[asignatura] = promedio
    return promedios

matematicas = [5, 3, 2, 1]
ciencias = [4, 1, 3, 1]
sociales = [3, 2, 0, 5]

resultados = calcular_promedio(matematicas=matematicas, ciencias=ciencias, sociales=sociales)

for asignatura, promedio in resultados.items():
    print(f"El promedio de {asignatura} es: {promedio}")
