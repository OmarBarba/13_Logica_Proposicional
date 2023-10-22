#logica modal
print("logica modal")
# Definimos un mundo posible
mundo_posible = {
    "llueve": True,
    "sol": False
}

# Expresamos una afirmación modal usando "◻"
afirmacion_modal = "◻llueve"

# Evaluamos la necesidad
if afirmacion_modal[1:] in mundo_posible and mundo_posible[afirmacion_modal[1:]]:
    resultado = "La afirmación es necesaria en este mundo posible."
else:
    resultado = "La afirmación no es necesaria en este mundo posible."

# Mostramos el resultado
print(resultado)

######################logica temporal 
print("logica temporal")
# Secuencia de eventos
secuencia_eventos = ["evento_A", "evento_B", "evento_C"]

# Expresamos una afirmación temporal usando "F"
afirmacion_temporal = "evento_A F evento_C"

# Evaluamos la afirmación temporal
if afirmacion_temporal in " ".join(secuencia_eventos):
    resultado = "La afirmación temporal se cumple en la secuencia de eventos."
else:
    resultado = "La afirmación temporal no se cumple en la secuencia de eventos."

# Mostramos el resultado
print(resultado)
################logica difusa
print("logica difusa")


# Funciones de pertenencia
def funcion_pertenencia_fria(temperatura):
    if temperatura <= 15:
        return 1.0
    elif 15 < temperatura < 20:
        return (20 - temperatura) / 5
    else:
        return 0.0

def funcion_pertenencia_caliente(temperatura):
    if temperatura >= 25:
        return 1.0
    elif 20 < temperatura < 25:
        return (temperatura - 20) / 5
    else:
        return 0.0

# Reglas difusas
def regla_fria(temperatura):
    return funcion_pertenencia_fria(temperatura)

def regla_caliente(temperatura):
    return funcion_pertenencia_caliente(temperatura)

# Inferencia basada en reglas
def calcular_potencia_calefaccion(temperatura):
    potencia_fria = regla_fria(temperatura)
    potencia_caliente = regla_caliente(temperatura)

    return potencia_fria, potencia_caliente

# Temperatura actual
temperatura_actual = 18

# Aplicar inferencia
potencia_fria, potencia_caliente = calcular_potencia_calefaccion(temperatura_actual)

# Control del sistema de calefacción
if potencia_fria > potencia_caliente:
    print("Encender calefacción fría")
else:
    print("Encender calefacción caliente")
