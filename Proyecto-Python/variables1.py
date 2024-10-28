# NOMBRES ADITIVOS DE VARIABLES

# 1.  Pueden empezar con una letra o un guión bajo (underscore)

mivariable = "texto"
_mivariable = 'otro texto'
MiOtraVariable = """
otro texto más
"""

# 2. No puede iniciar con un numero
### 5variable = "texto"

# 3. Sólo pueden contener caracteres alfanumericos y guiones bajos (A-z 0-9 _)
miVariable123_ ="texto"
_123miVariable = "texto"

# 4. CaseSensitive (no solo al comienzo sino en general)

miVariable = "otro texto"
MiVariable = "otro texto"

# 5. No se puede utilizar palabras reservadas de Python (keywords)

##############

# convenciones de escritura 

# Camel case
camelCase = "Comienza con minúscula y cada palabra siguiente comienzará con mayuscula"

# Pascal Case 
Pascalcase = "Comienza con mayúscula y cada palabra siguiente comenzará con mayúscula"

# Snake Case
snake_case = "Se usan las palabras en minúscula y las palabras son separadas con guiones bajos"

###############

# Multiasignacion 

x,y,z = 5,7,9 #(se pueden asignar varias variable en la misma linea de codigo)

a = b = c = "Sergie Code"

# Multiasignacion de Colecciones

frutas = ["naranja", "banana", "manzana"]
m, n, o = frutas

# Uso de print y salidas:

txt = "Cuerso"
txt2 = "de"
txt3 = "Python"

# print(txt, txt2, txt3)
# print(txt + txt2 +txt3)

num1 = 2
num2 = 4
num3 = 6

#print(num1, num2, num3) concatena los numeros de las variables
#print(num1 + num2 + num3) suma los numeros de las variables

# Variables Globales vs Variables de Scope

variableGlobal = "Esta variable va a estar disponible para todo el programa"

def funcion():
    # global variableDeScope
    variableDeScope = "Esta variable solo estara disponible dentro del alcance da la funcion"
    variableGlobal = "Este valor es solo para dentro de la funcion y luego recupara su valor"
    print(variableGlobal)
    print(variableDeScope)

funcion()

print(variableGlobal)
# print(variableDeScope)