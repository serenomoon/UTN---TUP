def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i  
    return resultado

facto = factorial(5)
print(facto)
