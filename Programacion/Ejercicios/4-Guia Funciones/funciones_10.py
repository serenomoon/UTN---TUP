# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def es_primo(numero: int | float):
    for i in range(2,numero):
        if numero % i == 0:
            return False
        else:
            return True

calculo_es_primo = es_primo(23)
print(f"¿Es el numero primo?: {calculo_es_primo}")