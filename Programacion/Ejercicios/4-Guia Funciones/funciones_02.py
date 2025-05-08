# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def num_float():
    numero = float(input("Ingresá un número con coma: "))
    return numero

print(f"Numero float: {num_float()}")