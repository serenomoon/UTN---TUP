def crear_vector(contenido: any, dimension: int) -> list:
    """Crea un vector repitiendo el "contenido" en cada uno de los espacios defiinidos por "dimension"
    Args:
        contenido (any): Contenido que llenara los indices del array (Ej: None)
        dimension (int): Cantidad de indices o posiciones que tendra el array

    Returns:
        list: Devuelve una lista "cruda"
    """
    vector = [contenido] * dimension
    return vector


def agregar_valor_lista(lista: list, nuevo_valor):
    """Toma una lista, y crea una nueva con el tamaño de la ingresada + 1 y luego agrega todos los valores
    de la anterior, mas el nuevo valor


    Args:
        lista (list): Lista a "actualizar"
        nuevo_valor (_type_): Valor nuevo a insertar en la nueva lista

    Returns:
        _type_: Devuelve una nueva lista actualizada
    """
    nueva_lista = crear_vector(None, len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = nuevo_valor
    return nueva_lista


def valor_repetido(lista: list, valor) -> bool:
    """Itera una lista y se fija si el valor ingresado se encuentra dentro

    Args:
        lista (list): Lista a chequear
        valor (_type_): valor a chequear

    Returns:
        bool: Devuelve True si esta repetido
    """
    for i in range(len(lista)):
        if lista[i] == valor:
            return True
    return False