def crear_matriz(cantidad_columnas: int, cantidad_filas: int, valor_inicial: any = None) -> list:
    matriz2 = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz2 += [fila] 
    return(matriz2)

k = 5

matriz = [
    [3,5],
    [2,8],
    [4,3],
    ]

resultado = crear_matriz(len(matriz[0]), len(matriz))

# multiplicar matriz por K
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        resultado[i][j] = matriz[i][j] * k  #Ambas estan en la misma posicion en la matriz

print(resultado)