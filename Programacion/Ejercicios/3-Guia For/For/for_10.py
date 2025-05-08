# Ingresar un número. Determinar si el número es primo o no.
es_primo = True
numero_ingresado = int(input("Ingrese un numero: "))
for i in range(2,numero_ingresado):
    if numero_ingresado % i == 0:
        es_primo = False
        break

if es_primo:
    print(f"El numero {numero_ingresado} es primo")
else:
    print(f"El numero {numero_ingresado} no es primo")