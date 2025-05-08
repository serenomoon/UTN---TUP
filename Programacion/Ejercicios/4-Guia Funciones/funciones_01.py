# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def num_entero():
    numero = int(input("Ingresá un número entero: "))
    return numero

print(f"Numero entero: {num_entero()}")