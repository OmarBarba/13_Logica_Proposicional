import random

def funcion_objetivo(x):
    # Esta es la función que queremos optimizar.
    # En este ejemplo, simplemente es una función cuadrática.
    return -x**2 + 10*x + 20

def hill_climbing(iteraciones, paso, inicio):
    mejor_solucion = inicio
    mejor_valor = funcion_objetivo(inicio)
    
    for _ in range(iteraciones):
        vecino = mejor_solucion + random.uniform(-paso, paso)
        valor_vecino = funcion_objetivo(vecino)
        
        if valor_vecino > mejor_valor:
            mejor_solucion = vecino
            mejor_valor = valor_vecino
    
    return mejor_solucion, mejor_valor

# Parámetros del algoritmo
iteraciones = 1000
paso = 0.1
inicio = 5.0

# Ejecutar la búsqueda en ascenso
mejor_solucion, mejor_valor = hill_climbing(iteraciones, paso, inicio)

print("Mejor solución encontrada:", mejor_solucion)
print("Mejor valor encontrado:", mejor_valor)
