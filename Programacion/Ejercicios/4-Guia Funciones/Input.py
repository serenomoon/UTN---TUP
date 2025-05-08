from Validate import validate_number, validate_length

def get_init(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    resultado = None
    print(mensaje)
    numero = int(input(f"Ingrese un numero entero entre {minimo} y {maximo}: "))

    while reintentos > 1:
        if validate_number(numero,minimo,maximo,int):
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

numero_entero = get_float("Bienvenido!","Error!!,", 0, 10, 3)
print(numero_entero)
