####### STRING (Cadena de texto)
# from  import


texto = "Este es un cuurso de Pyton por Sergie Code"

#str (string): Texto o Cadena de caracteres
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimple = '''Este es un texto'''

####### TYPE 
# print(type(comillasSimples))

####### Arrays de caracteres
caracter = texto[4] # Podemos seleccionar un caracter por índice

####### Len (Length) (Saber el largo)
amplitud = len(texto)

# print(amplitud)

####### In: Para saber si esta incluido algo en el texto
# print("Pyton" in texto) # devuelve un True o False según corresponda

####### Not in: con la palabra reservada not podemos negar y pedir un resultado negativo
# print("JavaScript" not in texto) # devuelve un True o False según corresponda

# Slice (cortar) una parte del texto
# print(texto[0:5]) # "Este es"

# Moificadores de texto (mayúsculas, minúsculas, etc)

texto_con_espacios = "   hola mundo   "

mayusculas = texto.upper() # Obtendré el texto en mayúsculas
minusculas = texto.lower() #Obtendré el texto en minusculas
sin_espacios = texto_con_espacios.strip() #Eliminará los espacios del comienzo y el final
reemplazo = texto_con_espacios.replace("mundo", "universo") #Reemplazará mundo por universo

#Modificadores mas usados
texto_a_modificar = "este es UN texto A MODIFICAR"
capitalizado = texto_a_modificar.capitalize() # Sólo quedará la primera letra como mayúsculas
estaComenzando = texto_a_modificar.startswith("este")
estaFinalizando = texto_a_modificar.endswith("MODIFICAR")
titulo = texto_a_modificar.title() # Pone en mayúuscula cada palabra
contador = texto_a_modificar.count("e") # Cuantas veces aparece la e en el texto
buscador = texto_a_modificar.find("texto") # Nos devuelve el índice donde comienza la palabra buscada


# Concatenar
a = "Hola" 
b = "mundo"

concatenado = a + " " + b

# F-Strings (template strings)
num = 5
nombre = "Pedrito"
txt = f"La edad de {nombre} es de {num:.2f}" # Nos permite utilizar variables de texto y formatearlas

resultado = f"El resultado de 69 x 75 es {69*75}"

# print(txt)
# print(resultado)

# Escapes \ (backslash - barra invetida)
escape = "Mi pais favorito es \"Lituania\" por que me dio la ciudadanía europea"
salto_de_linea = "Quiero hacer un \nsalto de linea"

print(salto_de_linea)