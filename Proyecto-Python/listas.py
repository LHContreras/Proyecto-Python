# LISTAS: colección (arrays) que permite almacenar elementos en una sola variable 
# Caracteristicas: ordenada (podemos ingresar a un elemento por indice) y es mutable

# indices:    0          1         3       4
frutas = ["Naranja", "Manzana", "Pera", "Pera"] # Permite duplicados
longitud = len(frutas) # saber la cantidad de elementos que tiene una lista

listaString = ["alfa", "beta", "gamma"]
listaNumbers = [0, 1, 2, 3, 4]
listaBooleans = [True, True, False]
listaMixta = ["alfa", 1, False]

tipo = type(listaMixta) # Esto nos indicará que tipo de datos es: "list"

listaDesdeConstructor = list(('Beta', 2, True)) # Hay que utilizar el constructor list y doble parentesis

# Acceder a datos:

naranja = frutas[0]
parteLista = frutas[1:3] # Desde el 1(manzana) hasta el 3 (no inclusive)

# Verificar si existe un elemento

# if "Banana" in frutas:  # Utilizando la palabra "in" podemos saber si un elemento está presente
    # print("La fruta manzana está en la lista")

# Modificar datos:

tecnologias = ['Python', 'Django', 'Flask', 'ReactPy', 'Pandas']

tecnologias[3] = 'TensoFlow'  # Reemplazar el elemento de un indice particular
tecnologias[2:4] = ['NumPy', 'Scrapy'] # Reemplazar una parte de la lista

# Agregar elementos:
tecnologias.insert(2, 'Flask') # Insertar un nuevo elemento en un indice especifico
tecnologias.append('TensorFlow') # Agregamos un elemento nuuevo al final de la lista

frontend = ['Angular', 'React', 'Vue']

tecnologias.extend(frontend) # Agregar una lista a otra (fusíon)

# Quitar elementos:
tecnologias.remove('Vue') # Se remueve el eleento que coincida con lo que pasemos de agurmento
tecnologias.pop() # Podemos eliminr un eleento de un indice especifico y si no especificamos se eliminara el ultimo
del tecnologias[7] #Usando la palabra del podemos especificaar el elemento  eliminar

listaABorar = ['Python', 'Djongo', 'Flask', 'ReactPy', 'Pandas']
listaABorar.clear() # Vaciaría la lista

# Recorrer lista

# for tecnologia in tecnologias:
#     print(f"Tecnología: {tecnologia}")

# for i in range(len(tecnologias)): # De esta forma podemos tener el indice del elemento itereble al recorrer la lista
    # print(f"{i+1}. {tecnologias[i]}")

# [print(tecnologia) for tecnologia in tecnologias]  # Este seria el Shorthand para una impresion de lista iterable

# Ejemplo practico:

listaConY = []

for tecnologia in tecnologias:
    if "y" in tecnologia:
        listaConY.append(tecnologia)
 #          lo que agrega |  el bucle                 | laa condicion
listaConY = [tecnologia for ternologia in tecnologias if "y" in tecnologia]  # Shorthand del ejemplo de arriba

#Ordenar una lista
tecnologias.sort() # En caso de no especificar ordenara alfabeticaente o de forma ascendente
numeros = [7,9,5,3,8,6,4,2]
numeros.sort(reverse=True) # En este caso ordennara de forma descendiente
tecnologias.reverse() # Odenar exactamente al revés tal cual estaba la lista

# Copiar una lista:

meses = ['Enero', 'Febrerod', 'Marzo', 'Abril', 'Mayo']
meses2 = ['Junio', 'Julio', 'Agosto', 'Septiembre']
copiaMeses = meses.copy()
copiaMeses2 = list(meses) # Usando el constructor

joinMeses = meses + meses2 # Podemos jutar la listas (JOIN) utilizanndo el simbolo +
meses.extend(meses2)


print(numeros)

# print(tecnologias)