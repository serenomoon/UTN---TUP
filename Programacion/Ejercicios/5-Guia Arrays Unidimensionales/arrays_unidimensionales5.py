# Escribir una función que calcule y retorne el producto de todos los 
# elementos de la lista que recibe como parámetro.

def calculo_producto(enteros: list) -> float:
    """Calcula el producto de todos los numeros de un array

    Args:
        enteros (list): Array de numeros

    Returns:
        float: Devuelve el producto
    """
    producto = 1
    for i in range(len(enteros)):
        producto *= enteros[i]
    return producto