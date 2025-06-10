# Los sets no aceptan valores repetidos
# Se crean de dos formas:

mi_set = set() # Le puedo añadir una lista y la convierto
mi_set = {4,6,7,5,2,3,4,5} # Si imprimo esto, los valores repetidos desaparecen 
# y los ordena aleatoriamente.
# No tienen indice (mi_set[0]), pero se puede iterar con un for

# AGREGAR ELEMENTOS
mi_set.add(99) # Agrega un elemento, lo pone en un indice aleatorio

# QUITAR ELEMENOTOS
mi_set.remove(99) # Si pongo algo q no esta me tira error

mi_set.discard(6) # De esta forma no

mi_set.pop() # Elimina el primero, no es seguro si agregue algo nuevo, xq los reordenaria al agregar
# retorna el eliminado

mi_set.clear() # Lo vacia


# ENCONTRAR INTERSECCION ENTRE 2 SETS
set_1 = {5,4,9,3}
set_2 = {2,5,4,1}

inter = set_1.intersection(set_2)
print(inter) # Mostraria el 5 y el 4


# UNION ENTRE 2 CONJUNTOS (La suma)
union = set_1.union(set_2)
print(union) # Mostraria todos los datos dentro de ambos sets sin los repetidos


# DIFERENCIA ENTRE AMBOS SETS
diferencia_set1 = set_1.difference(set_2)
print(diferencia_set1) # Mostraria el 9 y el 3

diferencia_set2 = set_2.difference(set_1)
print(diferencia_set2) # Mostraria el 2 y el 1
