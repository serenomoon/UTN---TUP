# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números 
# primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la 
# cantidad de números primos encontrados. Modularizar todo lo posible.

def es_primo_check(index: int):
    for j in range(2,index):
        if index % j == 0:
            return False
    return True

def conteo_primos(numero: int | float):
    contador_primo = 0
    for i in range(2,numero+1):
        es_primo = es_primo_check(i)
        if es_primo:
            contador_primo += 1
    return contador_primo

def cant_primos(numero: int | float):
    contador = conteo_primos(numero)
    return contador

cantidad_primos = cant_primos(5)
print(f"La cantidad de primos es: {cantidad_primos}")