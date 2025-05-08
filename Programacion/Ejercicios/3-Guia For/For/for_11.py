# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
contador_primo = 0
numero_ingresado = int(input("Ingrese un numero: "))

for i in range(2,numero_ingresado+1):
    es_primo = True

    for j in range(2,i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El numero {i} es primo")
        contador_primo += 1

print(f"Total numeros primos: {contador_primo}")