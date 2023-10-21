# Crear una base de conocimiento utilizando diccionarios
base_de_conocimiento = {
    "persona1": {
        "nombre": "Alice",
        "edad": 30,
        "ocupacion": "Ingeniera de software"
    },
    "persona2": {
        "nombre": "Bob",
        "edad": 25,
        "ocupacion": "Diseñador gráfico"
    },
    "libro1": {
        "titulo": "Introducción a la Inteligencia Artificial",
        "autor": "John Smith",
        "anio_publicacion": 2020
    }
}

# Acceder al conocimiento
persona1 = base_de_conocimiento["persona1"]
nombre_persona1 = persona1["nombre"]
print(f"Nombre de persona1: {nombre_persona1}")

libro1 = base_de_conocimiento["libro1"]
titulo_libro1 = libro1["titulo"]
print(f"Título de libro1: {titulo_libro1}")
