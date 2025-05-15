from Validate import validate_number, validate_length

def get_init(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int = 999) -> int | None:
    """Valida si un numero coincide con las especificaciones del usuario

    Args:
        mensaje (str): Mensaje mostrado antes de ingresar un numero
        mensaje_error (str): Mensaje de error que se muestra al no coicidir el numero con los parametros deceados
        minimo (int): Minimo valor al que el numero puede llegar
        maximo (int): Maximo  valor al que el numero puede llegar
        reintentos (int, optional): Reintentos que tiene el usario para ingresar un numero correcto. Defaults to 999.

    Returns:
        int | None: Devuelve el numero de ser correcto, None si la cantidad de intentos es superada
    """
    resultado = None
    print(mensaje)
    numero = int(input(f"Ingrese un numero entero entre {minimo} y {maximo}: "))

    while reintentos > 1:
        if validate_number(numero,int,minimo,maximo):
            resultado = numero
            break
        else:
            numero = int(input(f"{mensaje_error} reingrese el numero entero entre {minimo} y {maximo}: "))
            reintentos -= 1

    if resultado is None:
        print(f"{mensaje_error} numero de intentos superado.")
    return resultado


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    resultado = None
    print(mensaje)
    numero = float(input(f"Ingrese un numero decimal entre {minimo} y {maximo}: "))

    while reintentos > 1:
        if validate_number(numero,minimo,maximo,float):
            resultado = numero
            break
        else:
            numero = float(input(f"{mensaje_error} reingrese el numero decimal entre {minimo} y {maximo}: "))
            reintentos -= 1

    if resultado is None:
        print(f"{mensaje_error} numero de intentos superado.")
    return resultado


def get_string(longitud: int, mensaje: str, mensaje_error: str, reintentos: int) -> str | None:
    resultado = None
    print(mensaje)

    while reintentos > 0:
        cadena = input(f"Ingrese una cadena de {longitud} caracteres: ")

        if validate_length(cadena,longitud):
            resultado = cadena
            break
        else:
            print(f"{mensaje_error} la cadena debe tener {longitud} caracteres.")
            reintentos -= 1

    if resultado is None:
        print(f"{mensaje_error} numero de intentos superado.")

    return resultado

