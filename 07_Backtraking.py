def es_seguro(tablero, fila, columna):
    # Verificar si no hay reinas en la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar si no hay reinas en la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar si no hay reinas en la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, len(tablero))):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, fila):
    if fila == len(tablero):
        return True  # Todas las reinas están ubicadas

    for columna in range(len(tablero)):
        if es_seguro(tablero, fila, columna):
            tablero[fila][columna] = 1  # Coloca una reina en la casilla
            if resolver_n_reinas(tablero, fila + 1):
                return True  # Si se encontró una solución válida
            tablero[fila][columna] = 0  # Retrocede si no se encontró una solución válida

    return False  # No se encontró una solución válida

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if x == 1 else "." for x in fila))

# Tamaño del tablero de ajedrez
n = 8

# Inicializar el tablero
tablero = [[0 for _ in range(n)] for _ in range(n)]

# Resolver el problema de las N reinas
if resolver_n_reinas(tablero, 0):
    print("Solución encontrada:")
    imprimir_tablero(tablero)
else:
    print("No se encontró una solución.")

