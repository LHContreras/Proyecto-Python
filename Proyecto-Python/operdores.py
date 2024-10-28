##### OPERADORES: Símboos que nos permitíran hacer operaciones sobre variables y valores

## Operedores aritmeticos (+, -, *, /, %, **, //)

a = 5
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b # devuelve flotante(con decimales)
floorDivision = a // b # devuelve uun entero
resto = a % b # Resto de la divicion
exponenciales = a ** b

## Operadores de Asignacion

x = 5 # El = es el operador de asignacion mas basico
x += 3 # x = x + 3
x -= 2 # x = x - 2
x *= 4 # x = x * 4
x /= 2 # x = x / 2

## Operadores logicos (AND, OR, NOT)

edad = 17
tramite = edad >=18 and edad <= 65 ## Devuelve True si cumplimos las 2 condiciones dadas
semaforo = "Rojo"
cruzar = semaforo == "Verde" or semaforo == "Amarillo" ## Devuelve True si cumplimos al menos una de las dos condiciones
verdad = True
print(not verdad) ## Niega la estructura siguiente

## Operadores de comparacion ( nos devolveran True o False)

num1 = 6
num2 = 5
igualdad = num1  == num2 # Devuelve True si son iguales
distinto = num1 != num2  # Devuelve True si son distintos
mayor = num1 > num2 # Devuelve True si es Mayor
menor = num1 < num2 # Devuelve True si es Menor
mayorIgual = num1 >= num2 # Devuelve True si es Mayorr o Igual
menorIgual = num1 <= num2 # Devuelve True si es Menor o Igual


## Operadores de identidad (is ,is not)

nombre = "Sergie Code"
profesor = "Sergie Code"
alumno = "Pedrito"
sonElMismo = nombre is profesor # Nos devuelve True si son iguales
sonDistinto = profesor is not alumno # Nos devuelve True si son distinto

## Operadores de pertenencia (in, not in)

palabra = "Mundo"
palabra2 = "Mercurio"
texto = "Hola Mundo"
pertenece = palabra in texto # Nos devuelve True si pertenece
noPertenece = palabra2 not in texto # Nos devuelve True si no está presente