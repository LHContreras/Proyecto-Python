# int (Integer): Número entero
numero_entero = 1

# float: Número decimal
numero_decimal = 3.14

#  complex: Número complejo (parte entera y otra parte imaginaria)
numero_complejo = 5 + 2j

# print(numero_entero)
# print(type(numero_entero)) #int

# print(numero_decimal)
# print(type(numero_decimal)) #float

# print(numero_complejo)
# print(type(numero_complejo)) #complex

###### CASTEO

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

####### RANDOM

import random

aleatorio = random.randrange(1,10) # El número de stop no es incluyente
aleatorio_par = random.randrange(2,11,2) # Número par del 2 al 10(incluído)
aleatorio_inpar = random.randrange(1,10,2) # Número impar del 1 al 9 (incluído) 
