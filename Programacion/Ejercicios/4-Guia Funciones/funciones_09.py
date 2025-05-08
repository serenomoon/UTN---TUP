# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente 
# como argumentos y devolver el resultado.
def calc_potencia(base: int | float, exponente: int | float):
    potencia = base**exponente
    return potencia

calculo_potencia = calc_potencia(5,2)
print(f"La potencia calculada es: {calculo_potencia}")