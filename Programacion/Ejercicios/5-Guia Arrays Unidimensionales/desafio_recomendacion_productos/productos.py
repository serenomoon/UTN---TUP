from array_dinamico import *

def productos_en_comun(cliente1: list, cliente2: list, cliente3: list) -> list:
    en_comun = crear_vector(None, 0)

    for i in range(len(cliente1)):
        valor = cliente1[i]

        esta_en_cliente2 = False
        for j in range(len(cliente2)):
            if valor == cliente2[j]:
                esta_en_cliente2 = True
                break

        esta_en_cliente3 = False
        for k in range(len(cliente3)):
            if valor == cliente3[k]:
                esta_en_cliente3 = True
                break

        if esta_en_cliente2 and esta_en_cliente3:
            ya_esta = False
            for m in range(len(en_comun)):
                if valor == en_comun[m]:
                    ya_esta = True
                    break
            if not ya_esta:
                en_comun = agregar_valor_lista(en_comun, valor)

    return en_comun


def productos_exclusivos(cliente1: list, cliente2: list, cliente3: list) -> list:
    productos_exclusivos = crear_vector(None, 0)

    for i in range(len(cliente1)):
        valor = cliente1[i]
        esta_en_cliente2 = False
        esta_en_cliente3 = False

        for j in range(len(cliente2)):
            if valor == cliente2[j]:
                esta_en_cliente2 = True
                break

        for k in range(len(cliente3)):
            if valor == cliente3[k]:
                esta_en_cliente3 = True
                break

        if not esta_en_cliente2 and not esta_en_cliente3:
            productos_exclusivos = agregar_valor_lista(productos_exclusivos, valor)


    for i in range(len(cliente2)):
        valor = cliente2[i]
        esta_en_cliente1 = False
        esta_en_cliente3 = False

        for j in range(len(cliente1)):
            if valor == cliente1[j]:
                esta_en_cliente1 = True
                break

        for k in range(len(cliente3)):
            if valor == cliente3[k]:
                esta_en_cliente3 = True
                break

        if not esta_en_cliente1 and not esta_en_cliente3:
            productos_exclusivos = agregar_valor_lista(productos_exclusivos, valor)


    for i in range(len(cliente3)):
        valor = cliente3[i]
        esta_en_cliente1 = False
        esta_en_cliente2 = False

        for j in range(len(cliente1)):
            if valor == cliente1[j]:
                esta_en_cliente1 = True
                break

        for k in range(len(cliente2)):
            if valor == cliente2[k]:
                esta_en_cliente2 = True
                break

        if not esta_en_cliente1 and not esta_en_cliente2:
            productos_exclusivos = agregar_valor_lista(productos_exclusivos, valor)

    return productos_exclusivos



def productos_totales(cliente1: list, cliente2: list, cliente3: list) -> list:
    total_productos = crear_vector(None, 0)

    for i in range(len(cliente1)):
        if not valor_repetido(total_productos, cliente1[i]):
            total_productos = agregar_valor_lista(total_productos, cliente1[i])

    for i in range(len(cliente2)):
        if not valor_repetido(total_productos, cliente2[i]):
            total_productos = agregar_valor_lista(total_productos, cliente2[i])

    for i in range(len(cliente3)):
        if not valor_repetido(total_productos, cliente3[i]):
            total_productos = agregar_valor_lista(total_productos, cliente3[i])

    return total_productos



def recomendacion(cliente1: list, cliente2: list, cliente3: list) -> list:
    recomienda = crear_vector(None, 0)

    for i in range(len(cliente2)):
        valor = cliente2[i]
        if not valor_repetido(cliente1, valor) and not valor_repetido(recomienda, valor):
            recomienda = agregar_valor_lista(recomienda, valor)

    for i in range(len(cliente3)):
        valor = cliente3[i]
        if not valor_repetido(cliente1, valor) and not valor_repetido(recomienda, valor):
            recomienda = agregar_valor_lista(recomienda, valor)

    return recomienda