
# Definimos las posibles asignaciones de valores de verdad para p y q
posibles_valores = [True, False]

# Encabezado de la tabla de verdad
print("p | q | p ∧ q")
print("--|---|------")

# Generamos todas las combinaciones posibles de valores de verdad para p y q
for p in posibles_valores:
    for q in posibles_valores:
        # Calculamos el valor de verdad de la expresión "p ∧ q"
        resultado = p and q
        
        # Imprimimos la fila de la tabla de verdad
        print(f"{p} | {q} | {resultado}")

# Fin de la tabla de verdad
