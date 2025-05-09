vector_a = [4,7,9,6,3]
vector_b = [5,3,2,9,3]

vector_resultado = [5,7,9,9,3] #Que guarde los mas grandes de vactor_a[i] y vector_b[i]
# Son paralelos cuando se corresponenden con la misma posicion cada uno. 
# Ej: vector_a[0] -> vector_b[0]
# Llamado "Modelo de Datos" 
# (Vectores paralelos -> Matrices + Vectores paralelos -> Diccionarios y Listas -> Objetos y Colecciones)

vector_c = [None] * 5

# Si son iguales guarde None:
for i in range(len(vector_c)):
    if vector_a[i] > vector_b[i]:
        vector_c[i] = vector_a[i]
    elif vector_a[i] < vector_b[i]:
        vector_c[i] = vector_b[i]
    else:
        vector_c[i] = None
print(vector_c)