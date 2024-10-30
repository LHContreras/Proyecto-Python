# Tupla : coleccion (Array) que permite almacenar múltiple elemmntos en una sola variable
# Caracteristica: Colleccion ordenada e inutable de elementos (cada elemento tendra un indice)

# Indices:       0           1       2        3          4
vehiculos = ("Bicicleta", "Moto", "Auto" "Camioneta", "Camion", "Avion", "Barco")

lonngitud = len(vehiculos) #  con len podemos saber la longitud de la tupla
tipo = type(vehiculos) # nos indica que es de tippo <class 'tuple'>
tuplaConstructor = tuple(("Esta", "es", "una", "tupla"))

# Acceso a traves de indices:
elemento1 = [1]
elemento2 = [-4]
rango = vehiculos[3:4]
desdeInicio = vehiculos[:3]
hastaFinal = vehiculos[3:]

# ¿Como puedo hacer para obtener una tupla con las caracteristicas que yo nececito?

listaVehiculos = list(vehiculos) # en una nueva variable volcar la tupla como lista
listaVehiculos[3] = "Carro" # hacer el cambio que queriamos hacer
listaVehiculos.append("Crucero")
listaVehiculos = tuple(listaVehiculos) # asignar a la tupla la lista modificada conertida en tupla

# Desemaquetamiento:
# (a,b,c,d,e,f,g) = vehiculos # asignará cada elemento a una variable correspondiente a la posicion
# (bici,moto, *cuatroRuedas, avion, barco, crucero) = vehiculos # con el asterisco podemos agrupar parte del desempaquetamiento

# Recorrer las tupplas con bucles

# for vehiculo in vehiculos:
    # print(vehiculo)

# for i in range(len(vehiculos)): # De esta forma podemos tener el indice del elemmento itinirable al recorrer la lista
    # print(f"{i+1}. {vehiculos[i]}")

[print(tecnologia) for tecnologia in vehiculos]

# Join de truplas (unir tuplas)

citricos  = ( "naranja", "limon", "popmelo")
tropicales = ("papaya", "coco")

frutas = citricos + tropicales  # con esto unimos las dos tuplas en una sola tupla 

print(frutas)
