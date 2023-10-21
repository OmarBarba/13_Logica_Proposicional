# Definimos dos proposiciones
p = True  # La primera parte de la afirmación condicional
q = False  # La segunda parte de la afirmación condicional

# Definimos la afirmación condicional "si p, entonces q"
afirmacion_condicional = p and (not p or q)

# Aplicamos la regla de la modus ponens
if p:
    if afirmacion_condicional:
        resultado = q
    else:
        resultado = "No se cumple la afirmación condicional."
else:
    resultado = "No se puede aplicar la modus ponens, ya que la primera parte (p) es falsa."

# Mostramos el resultado
print("Resultado de la inferencia:")
print(resultado)
