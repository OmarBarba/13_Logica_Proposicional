import sympy as sp

# Símbolos proposicionales
p, q = sp.symbols('p q')

# Definir dos fórmulas lógicas
formula1 = sp.Eq(p, sp.And(p, q))  # Ejemplo: p ⇔ (p ∧ q)
formula2 = sp.Eq(q, sp.Or(p, q))   # Ejemplo: q ⇔ (p ∨ q)

# Equivalencia
equivalencia = formula1.equals(formula2)
if equivalencia:
    print("Las fórmulas son equivalentes.")
else:
    print("Las fórmulas no son equivalentes.")

# Validez
validez_formula1 = sp.validity(formula1)
validez_formula2 = sp.validity(formula2)

if validez_formula1:
    print("La fórmula 1 es válida.")
else:
    print("La fórmula 1 no es válida.")

if validez_formula2:
    print("La fórmula 2 es válida.")
else:
    print("La fórmula 2 no es válida.")

# Satisfacibilidad
solucion_formula1 = sp.solve(formula1)
solucion_formula2 = sp.solve(formula2)

if solucion_formula1:
    print("La fórmula 1 es satisfacible.")
else:
    print("La fórmula 1 no es satisfacible.")

if solucion_formula2:
    print("La fórmula 2 es satisfacible.")
else:
    print("La fórmula 2 no es satisfacible.")
