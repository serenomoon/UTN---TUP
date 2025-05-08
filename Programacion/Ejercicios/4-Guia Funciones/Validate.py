#Puse numero_type segundo para que sea mas facil de utilizar cuando no hay minimos ni maximos.
def validate_number(numero: float | int, numero_type: float | int = int, minimo: float | int = None, maximo: float | int = None) -> bool:
    numero_validado = False

    if type(numero) == numero_type:
        if minimo != None and maximo != None:
            if minimo <= numero <= maximo:
                numero_validado = True
        else:
            numero_validado = True

    return numero_validado

def validate_length(cadena: str, longitud: int) -> bool:
    cadena_validada = False
    if len(cadena) == longitud:
        cadena_validada = True
    return cadena_validada

