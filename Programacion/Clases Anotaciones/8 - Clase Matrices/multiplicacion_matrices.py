matriz_a = [
    [2,3],
    [4,1],
    [5,2],
]

matriz_b = [
    [2,2,1],
    [1,0,1],
]

def multiplicar_matrices(matriz_a,matriz_b):
    matriz_resultado = [[0] * len(matriz_a) for _ in range(len(matriz_b[0]))]
    if len(matriz_a[0]) == len(matriz_b): # Verificamos que se puedan multiplicar las matrices
        for i in range(len(matriz_resultado)):
            for j in range(len(matriz_resultado[i])):
                for k in range(len(matriz_b)): #puedo poner matriz_a[i] tmb, columnas de a = filas de b
                    matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_resultado

resultado = multiplicar_matrices(matriz_a,matriz_b)
print(resultado)