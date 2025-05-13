# Desarrollar una función que permita crear un array de números con 
# la cantidad de elementos que establezca el parámetro recibido.

def crear_array(cantidad: int) -> list:
    """Crea una lista

    Args:
        cantidad (int): la cantidad de numeros que quiero en la lista

    Returns:
        _type_: devuelve el array obtenido
    """
    array = list(range(cantidad))
    return array
