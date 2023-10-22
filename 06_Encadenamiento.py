import heapq

# Definición de un grafo con nodos y conexiones
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Función para encontrar la ruta más corta utilizando el algoritmo A*
def encontrar_ruta_mas_corta(grafo, inicio, objetivo):
    frontera = [(0, inicio)]
    visitados = set()

    while frontera:
        costo, nodo_actual = heapq.heappop(frontera)

        if nodo_actual == objetivo:
            return costo

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        for vecino, costo_vecino in grafo[nodo_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + costo_vecino
                heapq.heappush(frontera, (nuevo_costo, vecino))

    return float('inf')  # No se encontró una ruta

# Ubicaciones
inicio = 'A'
objetivo = 'D'

# Encontrar la ruta más corta
costo_ruta = encontrar_ruta_mas_corta(grafo, inicio, objetivo)

if costo_ruta != float('inf'):
    print(f"La ruta más corta desde {inicio} a {objetivo} tiene un costo de {costo_ruta}.")
else:
    print(f"No hay una ruta válida desde {inicio} a {objetivo}.")
