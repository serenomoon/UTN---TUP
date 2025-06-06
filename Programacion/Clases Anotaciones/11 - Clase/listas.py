lista = [5,6,9]
# 5 es indice 0 pero tambien podria ser indice -3
# 6 es indice 1 pero tambien podria ser indice -2
# 6 es indice 2 pero tambien podria ser indice -1
# Podemos contar de adelante para atras tmb


# AGREGAR ELEMENTOS A LA LISTA ###################

lista.append(7) #A grega un elemento al final de la lista
lista.append("7") #Las listas son eterogeneas, le puedo agregar otro tipo de dato, no es lo ideal
# print = [5,6,9,7,"7"]

lista.insert(2, 99) # parametro1 = indice de la lista, parametro2 = dato a agregar en la lista.
# print = [5,6,99,9,7,"7"]

otra_lista = [3,6,7]
lista.extend(otra_lista) # Añade otra lista a la lista
# print = [5,6,99,9,7,"7",3,6,7]


#ELIMINAR ELEMENTOS DE LA LISTA ##################
lista2 = [3,5,9,8,7,1,5]
lista2.remove(5) # Recibe el valor a eliminar, elimina el primero que coincida
#Si hago remove de algo q no existe, se rompe (luego servira cuando usemos except catch de errores)

lista2.pop(3) # Elimina un elmento segun el indice que le indique, si no pongo nada, saca el ultimo
#tambien retorna que es lo q eliminó


#OTROS METODOS ##################
lista2.index(5) # Me devuelve el indice donde se encuentra el primer elemento que coincida

lista2.reverse() # Da vuelta la lista, modifica la variable

lista2.sort() # Ordena la lista de menor a mayor, le puedo pasar "reverse = True" como parametro
# llama al metodo reverse y lo ordena de mayor a menor

otra = lista
otra.sort() # Modifica tambien "lista", xq otra es una referencia, apunta al mismo lugar
# entonces:
import copy

copia = copy.copy(lista) # Hace una copia aparte, con otro ID, llamada Shallow copy
copia.sort() # Ahora solo modificaria la copia siperficial
# La copia es superficial, si quiero modificar algo mas complejo, me va a terminar 
# modificando la "lista"
# ej: 
lista = [[1,2],[3,4]]
copia2 = copy.copy(lista)
copia2[0] = [10,2] # Cambiaria el [1,2] por el [10,2]
copia2[0][1] = 1 # Cambiaria la copia y tambien la lista, el "2" por un "1"

# La mejor copia es:
copia = copy.deepcopy(lista) # Crea una nueva lista con los mismos valores y ya no tiene 
# relacion con la lista anterior

lista2.clear() #  Vacia la lista, sigue existiendo, mismo ID
lista2 = [] # Cambia el id de la variable, no asi con clear
del lista2 # La destruye, elimina la variable


#VARIANTE DE FOR LOOP
# for i in range(len(lista)):
#     print(lista[i])

# en vez de ese for, hacemos esto:

for numero in lista: #En vez de utilizar el rango como indice, obtiene de la lista cada  valor
    print(numero)



