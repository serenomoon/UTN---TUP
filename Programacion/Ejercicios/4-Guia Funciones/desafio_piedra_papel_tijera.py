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
# 🔹 Retorno:
# True → Si la partida sigue en curso.
# False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).

# 3️⃣ verificar_ganador_partida(aciertos_jugador, aciertos_maquina) → str
# 📌 Objetivo: Determina quién ganó la partida comparando los aciertos finales.
#  🔹 Parámetros:
# aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
# aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.
# 🔹 Retorno:
# "Jugador" → Si el jugador tiene más aciertos.
# "Máquina" → Si la máquina tiene más aciertos.

# 4️⃣ mostrar_elemento(eleccion) → str
# 📌 Objetivo: Convierte la elección numérica en un texto legible.
#  🔹 Parámetros:
# eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).
# 🔹 Retorno:
# "Piedra" cuando su elección == 1.
# "Papel" cuando su elección == 2.
# "Tijera" cuando su  elección == 3.

# 5️⃣ jugar_piedra_papel_tijera() → str
# 📌 Objetivo: Gestiona toda la lógica del juego, usando las funciones anteriores.
#  🔹 Flujo de la función:
# Inicia una partida donde el jugador compite contra la máquina.
# En cada ronda, el jugador elige una opción y la máquina genera una elección aleatoria.
# Se determina el ganador de la ronda.
# Se verifica si la partida continúa o si alguien ha ganado.
# Al finalizar, la función devuelve quién ganó la partida ("Jugador" o "Máquina").
import random

def verificar_ganador_ronda(jugador, maquina):
    if jugador == maquina:
        resultado = "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        resultado = "Jugador"
    else:
        resultado = "Maquina"
    return resultado

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
    sigue = True
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        sigue = False
    if ronda_actual >= 4:
        sigue = False
    return sigue

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    else:
        return "Maquina"

def mostrar_elemento(eleccion):
    if eleccion == 1:
        return "Piedra"
    if eleccion == 2:
        return "Papel"
    return "Tijera"

def jugar_piedra_papel_tijera(aciertos_jugador = 0, aciertos_maquina = 0, ronda = 1, victorias_jugador = 0, victorias_maquina = 0):
    print(f"Ronda numero {ronda}")
    print("1 - Piedra\n2 - Papel\n3 - Tijera")
    jugador = int(input("Elige uno: "))
    maquina = random.randint(1, 3)

    print(f"Jugador eligio: {mostrar_elemento(jugador)}")
    print(f"Maquina eligio: {mostrar_elemento(maquina)}")

    ganador_ronda = verificar_ganador_ronda(jugador, maquina)
    print(f"Gano la ronda: {ganador_ronda}")

    if ganador_ronda == "Jugador":
        aciertos_jugador += 1
        victorias_jugador += 1
        victorias_maquina = 0
    elif ganador_ronda == "Maquina":
        aciertos_maquina += 1
        victorias_maquina += 1
        victorias_jugador = 0
    else:
        victorias_jugador = 0
        victorias_maquina = 0

    seguir = verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda)

    if victorias_jugador == 2 or victorias_maquina == 2:
        seguir = False

    if seguir:
        jugar_piedra_papel_tijera(aciertos_jugador, aciertos_maquina, ronda + 1, victorias_jugador, victorias_maquina)
    else:
        print("Resultado final:")
        print(f"Jugador: {aciertos_jugador}")
        print(f"Maquina: {aciertos_maquina}")
        print(f"Ganador de la partida: {verificar_ganador_partida(aciertos_jugador, aciertos_maquina)}")

