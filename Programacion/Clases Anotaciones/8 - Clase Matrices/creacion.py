from carga import mostrar_matriz

matriz = [[None] * 3 for _ in range(4)] # Comprension de listas (usamos _ por que el valor ej:i, no lo usariamos)

matriz = [[None] * 3] * 4 # Asi no es valido 
# Esto no crea una matriz de listas independientes, sino que crea múltiples referencias 
# a la misma lista interna, lo que genera comportamientos incorrectos cuando se modifica.

matriz2 = []
for i in range(4):
    fila = [None] * 3
    matriz2 += [fila] # Valido tambien

# repite [None] * 3 cuatro veces (4 filas, y 3 columnas)

def crear_matriz(cantidad_columnas: int, cantidad_filas: int, valor_inicial: any = None) -> list:
    matriz2 = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz2 += [fila] 
    return(matriz2)

def insertar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input(f"Ingrese el valor de [{i,j}]: ")


mat = crear_matriz(3,5)
insertar_matriz(mat)
mostrar_matriz(mat)







