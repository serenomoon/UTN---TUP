# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def num_maximo(num1: float | int, num2: float | int, num3: float | int):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

numero_maximo = num_maximo(8,5,6)
print(f"El numero mas grande es: {numero_maximo}")