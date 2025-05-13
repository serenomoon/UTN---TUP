def crear_matriz(cantidad_columnas: int, cantidad_filas: int, valor_inicial: any = None) -> list:
    matriz2 = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz2 += [fila] 
    return(matriz2)

matriz_a = [
    [3,5],
    [2,8],
    [4,3],
    ]

matriz_b = [
    [7,5],
    [3,8],
    [4,5],
    ]

resultado = crear_matriz(len(matriz_a[0]), len(matriz_a)) #por que tienen el mismo tamaño

# sumar matrices
for i in range(len(resultado)): #recorro cualquiera de las 3
    for j in range(len(resultado[i])):
        resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]  #Sumo ambas matrices

print(resultado)