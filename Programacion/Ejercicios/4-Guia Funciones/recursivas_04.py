# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
from Validate import validate_number
def fibonacci(numero: int):
    numero_fibonacci = None 
    
    if validate_number(numero):
        if numero >= 0:
            if numero == 0:
                numero_fibonacci = 0
            elif numero == 1:
                numero_fibonacci = 1
            else:
                valor1 = 0
                valor2 = 1
                for i in range(2, numero + 1):
                    numero_fibonacci = valor1 + valor2
                    valor1 = valor2
                    valor2 = numero_fibonacci
        else:
            print("Error!! El numero debe ser positivo")
    
    return numero_fibonacci




# Nota general: en cada ejercicio al ingresar un número, se tendrá que utilizar la función get_int del módulo Input
