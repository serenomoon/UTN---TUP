def suma_horizontal(matriz: list) -> int:
    suma = 0
    matriz_resultados = [[None]]* len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        matriz_resultados[i] = suma
        suma = 0 
    return matriz_resultados

def suma_vertical(matriz: list) -> int:
    suma = 0
    matriz_resultados = [[None]]* len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[j][i]
        matriz_resultados[i] = suma
        suma = 0 
    return matriz_resultados

def suma_diagonal(matriz: list) -> int:
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def suma_diagonal_invertida(matriz: list) -> int:
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][len(matriz)-1-i]
    return suma

def verificar_cuadrado_magico(matriz: list) -> bool:
    es_magico = False
    n = len(matriz)
    M = (n*(n**2+1))/2
    suma_hor = suma_horizontal(matriz)
    suma_ver = suma_vertical(matriz)
    if len(matriz) == len(matriz[0]):
        if suma_diagonal(matriz) == M and suma_diagonal_invertida(matriz) == M:
            for i in range(len(suma_hor)):
                if suma_hor[i] != M:
                    break
                else:
                    es_magico = True
            for i in range(len(suma_ver)):
                if suma_ver[i] != M:
                    es_magico = False
                    break
                else:
                    es_magico = True
    return es_magico