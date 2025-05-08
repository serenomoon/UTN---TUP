# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
# Por defecto es del 1 al 10.
def tabla_multi(numero: int | float, inicio: int | float = 1, fin: int | float = 10):
    print("Tabla de Multiplicar")
    for i in range(inicio, fin+1):
        print(f"{numero} x {i} = {numero*i}")

tabla_multi(5,2,8)