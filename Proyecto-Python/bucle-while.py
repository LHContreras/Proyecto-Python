## BUCLES: Estructura que se repite mientras la condicion sea verdadera
## BUCLE WHILE:


x = 1

## Este bucle se repite mientras x sea menor o igual a 10
# while x <= 10:
#      print(f" X vale {x}")
#     x += 1


# while x <= 10:
#     print(f"X vale {x}")
#     if x == 5:
#         break   ## Esto hace que salga del bucle
#     if x == 5:
#         continue ## saltea las líneas de acá en adelante
#     x += 1
# print(x)

## EJEMPLO PRACTICO
while True:
    print("No te olvides de suscribirte a mi canal")
    respuesta = input("Desea salir? (s/n)").strip().lower()
    if respuesta == "s":
        break
