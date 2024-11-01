# SETS: coleccion (array) que permite almacenar multiples elementos en una sola variable
# Caracteristicas: coleccion desordenada de elementos únicos y mutables [no permite duplicados
# * Se pueden agregar y eliminar elemento pero los elementos no son "cambiables" ya que no tienen un orden

conjunto = {1,1,2,2,3} # los elementos que esten duplicados seran omitidos

longitud = len(conjunto) # l longitud o cantidad de elementos del conjunto (no tomará en cuenta los duplicados)
tipo = type(conjunto) # para saber el tipo <class 'set'>
conjuntoConstructor = set(("Este", "es", "un", "conjunto")) # creamos n conjunto usando el constructor

# if "conjunto" in conjuntoConstructor: # podemos usar IN para saber si un elemento esta presente
    # print("si esta la palabra")

# Agregaar elementos a un conjunto (SET)

telefonos = {'Xiaomi', 'Samsung', 'Motorola'}
telefono2 = ['Huawei', 'Oneplus','Nokia', 'Xiaomi'] # puede ser cualquier coleccion

telefonos.add("Iphone") # Agregar un elemento

telefonos.update(telefono2) # Con updte sumamos otra coleccion(puede ser cualquier coleccion) a nuestro conjunto

# Eliminar elementos (al no tner un orden especifico hay que tener mcho cuidado en el borrado)

autos = { 'Ford', 'Peugeot', 'Fiat','Renault', 'Ferrari' }

autos.remove('Ferrari') # Se borra un elemento que coincida exactamente con lo pasado por argumento (da un error si no existe)
autos.discard('Fiat') # Se borra un elemento que coincida exactamente con lo pasado por argumento (no da un error si no existe)

autos.pop() # Elimina uno de forma aleatoria 

# Recorrer los elementos con bucles

tecnologias = {'Python', 'C#', 'Java', 'Node'}

# for tecnologia in tecnologias:
    # print(tecnologia)

# [print(tecnologia) for tecnologia in tecnologias] # Este seria el shorthand para ina impresion de conjunto iterable

# Join de conjuntos (Teoria de conjuntos de la matematica)
a = {1,2,3,4,5}
b = {1,3,5,7,9}

booleanos = { True, False}

# Union: devuelve todos los elementos de ambos conjuntos (a diferencia del upate no modifica el conjunto original)
u = a.union(b) # aceptas varias colecciones (pueden ser listas o tuplas)
u2 = a | b # es exactamente lo mismo que usar union

# Interseccion : va a devolver los elementos que tengan en comun ambos conjuntos
i = a.intersection(b)
i2 = a & b # es exactamente lo mismo que usar intersection

# a.intersection_update(b) # interseccion update modifica el conjunto original

# Comportamiento con booleanos:
booleanos__union = a.union(booleanos) # True y 1 se consideran el mismo valor por lo caul solo se agregara False 
booleanos_intersection = a.intersection(booleanos) # La unisca interseccion es True ya que se considera igual 1

# Diferencias: devolver los elementos del primer conjunto que no esten presentes en el otro conjunto
d1 = a.difference(b)
d2 = a - b # es exactamente lo mismo que usar difference

# Diferencias simétricas: devolver los elementos que están en uno de los conjuntos pero no en ambos
dsl = a.symmetric_difference(b)
dsl2 = a ^ b # es exactamente lo mismo que usar symmetric_difference

print(d1)