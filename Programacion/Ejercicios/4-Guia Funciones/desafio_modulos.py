# Módulos
# 1- Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

# def get_init(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
#     pass

# En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive)
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

# En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
def get_init(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    resultado = None
    print(mensaje)
    numero = int(input(f"Ingrese un numero entero entre {minimo} y {maximo}: "))

    while reintentos > 1:
        if minimo <= numero <= maximo:
            resultado = numero
            break

        numero = int(input(f"{mensaje_error} reingrese el numero entero entre {minimo} y {maximo}: "))
        reintentos -= 1

    if resultado is None:
        print(f"{mensaje_error} numero de intentos superado.")
    return resultado


# numero_entero = get_init("Bienvenido!","Error!!,", 0, 10, 3)
# print(numero_entero)

# Repetir el mismo procedimiento para un dato de tipo float.
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    resultado = None
    print(mensaje)
    numero = float(input(f"Ingrese un numero decimal entre {minimo} y {maximo}: "))

    while reintentos > 1:
        if minimo <= numero <= maximo:
            resultado = numero
            break

        numero = float(input(f"{mensaje_error} reingrese el numero decimal entre {minimo} y {maximo}: "))
        reintentos -= 1

    if resultado is None:
        print(f"{mensaje_error} numero de intentos superado.")
    return resultado


# numero_decimal = get_float("Bienvenido!", "Error!!,", 0.1, 10.1, 3)
# print(numero_decimal)


# 2- Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud 
# de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el 
# ejercicio (se puede extender):

# def get_string(longitud: int) -> str|None:
#     pass

# Nota: utilizar la función len.

def get_string(longitud: int, mensaje: str, mensaje_error: str, reintentos: int) -> str | None:
    resultado = None
    print(mensaje)

    while reintentos > 0:
        cadena = input(f"Ingrese una cadena de {longitud} caracteres: ")

        if len(cadena) == longitud:
            resultado = cadena
            break
        else:
            print(f"{mensaje_error} la cadena debe tener {longitud} caracteres.")
            reintentos -= 1

    if resultado is None:
        print(f"{mensaje_error} numero de intentos superado.")

    return resultado

texto = get_string(5, "Bienvenido!", "Error!!,", 3)
print("Resultado:", texto)


# Realizar los siguientes módulos:
# Input.py
# get_int()
# get_float()
# get_string()
# Validate.py
# validate_number()
# validate_length()

# Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.

# Crear un repositorio en github con su apellido y nombre junto con el texto funciones_input:
# Por ejemplo: scarafilo_german_funciones_input
# Dicho repositorio deberá ser privado. Agregar a sus profesores como colaboradores.

