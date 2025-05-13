# Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# a-Una lista de nombres (lista_nombres).
# b-Un nombre a buscar en la lista (nombre_antiguo).
# c-Un nombre de reemplazo (nombre_nuevo).
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int:
    """Reemplaza un nombre antiguo por uno nuevo y devuelve la cantidad de cambios realizados

    Args:
        nombres (list): Lista de nombres
        nombre_antiguo (str): Nombre a reemplazar
        nombre_nuevo (str): Nombre actualizado

    Returns:
        int: Devuelve cantidad de cambios
    """
    nombres_actualizados = 0
    for i in range(len(nombres)):
        if nombres[i] == nombre_antiguo:
            nombres[i] = nombre_nuevo
            nombres_actualizados += 1
    return nombres_actualizados
