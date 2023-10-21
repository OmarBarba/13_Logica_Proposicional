# Definición de una base de conocimiento con reglas lógicas
base_de_conocimiento = {
    "regla1": {
        "si": "tiene_patas y es_pequeño",
        "entonces": "es_un_insecto"
    },
    "regla2": {
        "si": "tiene_patas y no es_pequeño",
        "entonces": "es_un_mamífero"
    },
    "regla3": {
        "si": "no tiene_patas y tiene_aletas",
        "entonces": "es_un_pez"
    },
    # Agrega más reglas lógicas según sea necesario
}

# Función para clasificar animales basada en la base de conocimiento
def clasificar_animal(datos):
    for regla in base_de_conocimiento.values():
        condiciones = regla["si"].split(" y ")
        cumple_condiciones = all(condicion in datos for condicion in condiciones)
        if cumple_condiciones:
            return regla["entonces"]
    
    return "No se puede determinar la clasificación."

# Datos de entrada para clasificar un animal
datos_animal = {
    "tiene_patas": True,
    "es_pequeño": True,
    "tiene_aletas": False
}

# Clasificar el animal
resultado_clasificacion = clasificar_animal(datos_animal)
print(f"El animal se clasifica como: {resultado_clasificacion}")

