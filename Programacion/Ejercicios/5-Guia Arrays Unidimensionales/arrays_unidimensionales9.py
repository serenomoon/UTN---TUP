# Crear una función que reciba como parámetros dos arrays. 
# La función deberá mostrar la intersección de los dos arrays.
"""
                    U
    ----------------------------------
    |              M                 |
    |   j    -------------  N     i  |
    |        |       ----|----       |
    |        |   a   |   | g  |      |
    |        |       | b | l  |      |
    |        |   c   |   | e  |      |
    |        |       ----|----       |
    |        -------------           |                       
    |   f                         h  |
    ----------------------------------
"""
M = ["a","c","b"]
N = ["b","g","l","e"]

def interseccion(array_a: list, array_b: list):
    """Chequea que str coinciden en cada array y las imprime

    Args:
        array_a (_type_): Pimero array
        array_b (_type_): Segundo array
    """
    for i in range(len(array_a)):
        for j in range(len(array_b)):
            if array_a[i] == array_b[j]:
                print(array_a[i])

interseccion(M,N)