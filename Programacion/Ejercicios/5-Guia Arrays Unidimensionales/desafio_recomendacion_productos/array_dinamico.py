def crear_vector(valor_inicial, tamaño):
    return [valor_inicial] * tamaño

def agregar_valor_lista(lista: list, nuevo_valor):
    nueva_lista = crear_vector(None, len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = nuevo_valor
    return nueva_lista

def valor_repetido(lista: list, valor) -> bool:
        for i in range(len(lista)):
            if lista[i] == valor:
                return True
        return False