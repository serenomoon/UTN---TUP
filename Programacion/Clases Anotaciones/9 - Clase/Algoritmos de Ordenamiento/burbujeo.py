# Chequeamos si el () es mayor al []
# () > []
# Si es asi lo intercambiamos y pasamos al siguiente

#  5     1    4   3   2
# (0)   [1]   2   3   4

#  1     5    4   3   2
# (0)   [1]   2   3   4
 
#  1     5   4   3   2
# (0)    1  [2]   3   4

#  1     5   4   3   2
# (0)    1  [2]   3   4
 
#  1     5   4   3   2
# (0)    1   2  [3]   4
 
#  1     5    4   3   2
# (0)    1    2   3  [4]
 
# {1}    5    4   3   2 -> EJ: {} Ordenado
#  0    (1)  [2]   3  4

# {1}    4    5   3   2
#  0    (1)  [2]   3  4

# {1}    4    5   3   2
#  0    (1)   2  [3]  4

# {1}    3    5   4   2
#  0    (1)   2  [3]  4

# {1}    3    5   4   2
#  0    (1)   2   3  [4]

# {1}   {2}    5   4   3
#  0    (1)   2   3  [4]

# Etc....

# {1} {2} {3} {4}  5
#  0   1   2   3  (4) [] Si siguiese tiraria error de index

# {1} {2} {3} {4}   5  -> Tiene que llega [] hasta el ultimo y ((hasta el ante ultimo
#  0   1   2  (3)  [4]

# Para intercambiar valores usamos una variable extra:

A = 5
B = 1
C = 0 #variable extra

C = A
A = B
B = C

# A------>B  Swap de variables
# ^-- C <-|

# Ahora trabajamos con los tres paradigmas: Repetitivas, Condicionales y Secuenciales

import time #Para ver cuanto tarda cada uno

start = time.time()


lista = [5,1,4,3,2]


# De esta forma recorre la lista sumando 1+i para obviar el numero anterior
for i in range(0,len(lista)-1,1):
    for j in range(1+i,len(lista),1):
        if lista[i] > lista[j]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar

# De esta forma tambien funciona, pero recorre indices de mas
# for i in range(len(lista)):
#     for j in range(len(lista)):
#         if lista[i] < lista[j]:
#             auxiliar = lista[i]
#             lista[i] = lista[j]
#             lista[j] = auxiliar

end = time.time()
print((end - start)*1000000) #Lo multiplico por mil porque es un numero muy chiquito 

print(lista)

# Otros metodos:
# SelectionSort
# QuickSort
# MergeSort
# InsertionSort

