import sympy as sp

# Símbolos proposicionales
p, q, r = sp.symbols('p q r')

# Fórmula lógica
formula = sp.Eq(sp.Or(sp.Not(p), q), sp.And(sp.Or(r, p), sp.Not(q)))

# Convertir la fórmula a FNC
fnc_formula = sp.to_cnf(formula, True)

# Mostrar la fórmula original y la FNC
print("Fórmula original:", formula)
print("Fórmula en Forma Normal Conjuntiva (FNC):", fnc_formula)
