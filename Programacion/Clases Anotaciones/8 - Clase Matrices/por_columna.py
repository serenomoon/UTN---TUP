matriz = [
    [3,5,9],
    [2,1,8],
    [4,0,9],
    [2,1,4],
]

for j in range(len(matriz[0])):  #Para hacer la transpuesta de la matriz, pasar columnas a filas 
    for i in range(len(matriz)): #y filas a columnas
        print(matriz[i][j], end = "\t") 
    print("")


def crear_transpuesta(matriz):
    transpuesta = [[None for _ in range(len(matriz))] for _ in range(len(matriz[0]))]
    print(transpuesta)
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

trans = crear_transpuesta(matriz)
print(trans)
