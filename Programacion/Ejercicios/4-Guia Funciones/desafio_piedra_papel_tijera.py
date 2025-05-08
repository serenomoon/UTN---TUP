# Piedra, Papel o Tijera - Desafío de Programación
# El clásico juego de la infancia, donde dos jugadores eligen entre tres elementos y la victoria se determina según las siguientes reglas:
# Piedra aplasta Tijera → 🏆 Gana la Piedra
# Tijera corta Papel → 🏆 Gana la Tijera
# Papel envuelve Piedra → 🏆 Gana el Papel

# Si ambos jugadores eligen el mismo elemento, la ronda termina en empate.
# 📌 Reglas del Juego
# La partida se juega al mejor de 3 rondas.
# Si un jugador (humano o máquina) logra dos aciertos seguidos, la partida finaliza automáticamente.
# En caso de empate en las 3 rondas, el juego continuará hasta que haya un ganador.

# 📌 Funciones a desarrollar
# 1️⃣ verificar_ganador_ronda(jugador, maquina) → str
# 📌 Objetivo: Determina quién ganó la ronda según las elecciones del jugador y la máquina.
#  🔹 Parámetros:
# jugador (int): Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera).
# maquina (int): Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera).
# 🔹 Retorno:
# "Jugador" → Si el jugador gana la ronda.
# "Máquina" → Si la máquina gana la ronda.
# "Empate" → Si ambos eligen el mismo elemento.

# 2️⃣ verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) → bool
# 📌 Objetivo: Determina si la partida sigue en curso o ya ha finalizado.
#  🔹 Parámetros:
# aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
# aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.
# ronda_actual (int): Número de la ronda actual.
import random

def verificar_ganador_ronda(jugador, maquina):
    ganador = "Empate"
    if (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        ganador = "Jugador"
    elif jugador != maquina:
        ganador = "Maquina"
    return ganador

def verificar_estado_partida(aciertos_jugador = 0, aciertos_maquina = 0, ronda_actual = 1):
    print("\nINGRESA:\n1 - Piedra\n2 - Papel\n3 - Tijera")
    jugador = int(input("Eleccion: "))
    maquina = random.randint(1, 3)

    print(f"La máquina eligio: {maquina}")
    resultado = verificar_ganador_ronda(jugador, maquina)

    if resultado == "Jugador":
        aciertos_jugador += 1
    elif resultado == "Maquina":
        aciertos_maquina += 1

    print(f"Ganador del a ronda {ronda_actual}: {resultado}")
    print(f"PUNTAJES: Jugador {aciertos_jugador} - Maquina {aciertos_maquina}")

    if (aciertos_jugador == 2 or aciertos_maquina == 2) or (ronda_actual == 3 and aciertos_jugador != aciertos_maquina):
        print("\nPARTIDA FINALIZADA")
        if aciertos_jugador > aciertos_maquina:
            print("Ganador: Jugador")
        else:
            print("Ganador: Maquina")
    else:
        verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual + 1)

    return True


verificar_estado_partida()
