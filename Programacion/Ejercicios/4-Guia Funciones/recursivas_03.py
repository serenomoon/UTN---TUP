# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
from Validate import validate_number
def sumar_digitos(numero: int)->int:
    resultado = None
    if validate_number(numero):
        if numero < 10:
            resultado = numero 
        else:
            ultimo_digito = numero % 10
            resto = numero // 10
            suma = sumar_digitos(resto)
            resultado = ultimo_digito + suma

    return resultado

digitos = sumar_digitos(497)
print(digitos)