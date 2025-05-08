# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def num_check(numero: float | int):
    if numero % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"

numero_check = num_check(7)
print(numero_check)
