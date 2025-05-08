# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
def pedir_dato_y_tipo(dato:int|float|str, tipo: type) -> float|int|str:
    resultado = None
    if type(dato) == tipo:
        resultado = dato
    return resultado

pedir_datos = pedir_dato_y_tipo("Hola",str)
print(pedir_datos)
