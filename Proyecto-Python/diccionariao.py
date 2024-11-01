# DICCIONARIO: coleccion (array) que permite almacenar multiples elementos en uuna sola variable
# Caracteristicas: Coleccion de pares clave---valor(key-value) desordenada y mutable

from turtle import clear


diccionario = {
    "nombre": "Sergie Code",
    "yuotube": "www.youtube.com/@sergiecode",
    "tecnologias": ["Python", "JavaScript"],
    "edad": 34,
    "direccion": {"calle": "Av Argentina", "numero": 123, "ciudad": "Londes"},
}

tipo = type(diccionario) # Nos indica el tipo de datos <class 'dict'>
longitud = len(diccionario) # Nos indica la cantidad de clave-valor que tiene el diccionario
constructordiccionario = dict(nombre = "Sergie Code", youtube = "www.youtube.com/@sergiecode") # se puede crear con constructor

# ¿Como accedo a cada propiedad?

nombre = diccionario["nombre"]
youtube = diccionario.get("youtube")
keys = diccionario.keys() # el tipo de datos que devuelve se llama <class 'dict_keys>
values = diccionario.values() # el tipo de dato que devuelve se llama <class 'dict_values'>

items = diccionario.items() # nos devuelve tuplas de clave-valor en una lista // <class 'dict_items>

# CAMBIO de valores en un diccionario

diccionario["tecnologias"] = ['Python', 'JavaScript', 'Java', 'Node']
diccionario = ({"diccionario": {"calle": "Liverpool Street", "numero": 123, "ciudad": "Londres"}})

# ADREGAR ITEMS:

diccionario["profesion"] = "Pregramador"
diccionario.update({'Comida Favorita': 'Milanesa'})

# ELIMINAR ITEMS:

diccionario.pop("Comida Favorita") #  Eliminar un elemento puntual

# BUCLES (LOOPS) para diccionarios:

curso_python = {
    "nombre": "Curso Python",
    "dificultad": "Python Básico",
    "profesor": "Sergie Code",
    "duracion": "6 horas"
}

# for key in curso_python:  # el bucle for común hará un recorrido de las keys
    # print(f"{key.capitalize()}: {curso_python[key]}")

# for values in curso_python.values():  # este bucle recorrerá solo los valores
    # print(values)

# for x,y in curso_python.items():  # desempaqueto l tupla de cada uno de los elementos de la lista que devuelve items
    # print(x,y)

# COPIAS de diccionarios:

copia = curso_python.copy() # copia exacta pero apuntando a otra direccion de memoria
copia2 = dict(curso_python) # copia usando constructor

# DICCIONARIOS ANINADOS:

hijo1 = {
    "nombre": "Pedro",
    "edad": 5
}
hijo2 = {
    "nombre": "Juan",
    "edad": 7
}
hijo3 = {
    "nombre": "Maria",
    "edad": 9
}

familia = {
    "hijo1": hijo1,
    "hijo2": hijo2,
    "hijo3": hijo3,
}

nombreHijo1 = familia["hijo1"]["nombre"]

for x,obj in familia.items():
    print(x)
    for y in obj:
        print(f"{y.capitalize()}: {obj[y]}")