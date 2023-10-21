# Creamos una base de conocimiento representada como un diccionario
base_de_conocimiento = {
    "juan": "es un ingeniero",
    "maria": "es una doctora",
    "pedro": "es un abogado",
    "es_un_hombre": "juan",
    "es_una_mujer": "maria",
    "es_un_hombre": "pedro"
}

# Función para consultar la base de conocimiento
def consultar_conocimiento(nombre):
    if nombre in base_de_conocimiento:
        return base_de_conocimiento[nombre]
    else:
        return f"No tengo información sobre {nombre} en mi base de conocimiento."

# Consultas a la base de conocimiento
print(consultar_conocimiento("juan"))  # Devuelve: "es un ingeniero"
print(consultar_conocimiento("maria"))  # Devuelve: "es una doctora"
print(consultar_conocimiento("ana"))    # Devuelve: "No tengo información sobre ana en mi base de conocimiento."
