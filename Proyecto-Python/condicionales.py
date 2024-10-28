### CONDICIONALES (if, elif, else)
# Es la estructura que nos permite tomar un flujo u otro según una condición

a = 5
b = 9
c = 7

if a > b:
    print(f"{a} es mayor que {b}")
elif c > b:
    print(f"{c} es mayor que {b}")
else:
    print(f"{a} es menor que {b} y {c} es menor que {b}")

### SHORTHANDS 

a = 5
b = 7

if a > b: print(f"{a} es mayor que {b}") ## Shorthands

# Ejecucion si es verdadero | condición | Ejecución si es Falso 
print("B es mayor que A") if b > a else print("A es mayor que B") ## Shorthands de If + Else