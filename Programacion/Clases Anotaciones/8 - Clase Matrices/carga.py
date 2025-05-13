matriz = [
    [3,5,9], #--> Fila
    [2,1,8],
    [4,0,9],
    [2,1,4],
    #|
    #Columna
]

for i in range(len(matriz)): #Cuantas filas (cada una de las listas internas de la matriz)
    for j in range(len(matriz[i])): #Se puede poner i o 0 porque todas las filas deberian ser igual de largas
        # print(matriz[i][j]) # matriz[1][1] seria igual a 1 x ej, o matriz[2][1] seria 0. 
        print(f"{matriz[i][j]:>5}", end = " ") #\t es tabulacion, puedo poner " " si quiero tambien.
        #en este caso podemos usar tambien :>5 que justifica el texto a la derecha con un ancho de 5 caracteres,
        #si porngo <5 lo justificaria a la izquierda
    print("") #Usamos "" para hacer un salto de linea, que viene por default al final del print


def mostrar_matriz(matriz):
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])): 
            print(matriz[i][j], end = "\t") 
        print("")


