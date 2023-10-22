# Definición de una base de conocimiento con reglas lógicas
base_de_conocimiento = {
    "regla1": {
        "si": ["p", "q"],
        "entonces": "r"
    },
    "regla2": {
        "si": ["s", "t"],
        "entonces": "p"
    },
    "regla3": {
        "si": ["u"],
        "entonces": "s"
    },
    # Agrega más reglas lógicas según sea necesario
}

# Hechos iniciales
hechos = ["u"]

# Encadenamiento hacia adelante
def encadenamiento_hacia_adelante(base_conocimiento, hechos):
    nuevos_hechos = []
    while True:
        se_agregaron_nuevos_hechos = False
        for regla, datos in base_conocimiento.items():
            if set(datos["si"]).issubset(set(hechos)) and datos["entonces"] not in hechos:
                nuevos_hechos.append(datos["entonces"])
                se_agregaron_nuevos_hechos = True
        hechos.extend(nuevos_hechos)
        if not se_agregaron_nuevos_hechos:
            break
    return hechos

nuevos_hechos = encadenamiento_hacia_adelante(base_de_conocimiento, hechos)
print("Hechos derivados por encadenamiento hacia adelante:", nuevos_hechos)
