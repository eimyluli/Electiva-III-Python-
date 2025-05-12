import random

# CLASE PADRE
class Personaje:
    def __init__(self, nombre, descripcion, vida, ataques, defensas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vida = vida
        self.ataques = ataques
        self.defensas = defensas

    def atacar(self):
        ataque = random.choice(self.ataques)
        return ataque

    def defender(self):
        defensa = random.choice(self.defensas)
        return defensa

# Clase hijo (jugadors)
class Zeus(Personaje):
    def __init__(self):
        super().__init__(
            "Zeus",
            "Rey de los dioses, dios del cielo y el rayo.",
            100,
            [("Rayo celestial", 30), ("Tormenta divina", 20), ("Golpe de trueno", 15)],
            [("Escudo de rayos", 20), ("Esquivar", 10)]
        )

class Hera(Personaje):
    def __init__(self):
        super().__init__(
            "Hera",
            "Reina de los dioses.",
            110,
            [("Lazo del destino", 25), ("Gracia castigadora", 18), ("Grito de autoridad", 12)],
            [("Aura protectora", 18), ("Retroceso místico", 8)]
        )

class Atenea(Personaje):
    def __init__(self):
        super().__init__(
            "Atenea",
            "Diosa de la sabiduría, la guerra estratégica y las artes.",
            105,
            [("Lanza de sabiduría", 28), ("Táctica implacable", 19), ("Conjuro mental", 14)],
            [("Escudo aegis", 22), ("Postura defensiva", 9)]
        )

# Clases para enemigos
class Enemigo(Personaje):
    pass

enemigos = [
    Enemigo("Némesis", "", 100, [("Juicio divino", 25), ("Castigo oscuro", 18), ("Daga equilibrante", 14)],
            [("Justicia ciega", 18), ("Esquiva sombría", 9)]),
    Enemigo("Minotauro", "", 120, [("Embiste brutal", 30), ("Rugido ensordecedor", 20), ("Golpe con hacha", 15)],
            [("Piel gruesa", 20), ("Cubrebrazo tosco", 10)]),
    Enemigo("Titán Tifón", "", 130, [("Tormenta infernal", 35), ("Fuego de montaña", 22), ("Aliento de caos", 18)],
            [("Barrera titánica", 25), ("Resistencia salvaje", 12)])
]

def seleccionar_personaje():
    opciones = [Zeus(), Hera(), Atenea()]
    print("¡Elige tu personaje!\n")
    for i, p in enumerate(opciones):
        print(f"{i + 1}. {p.nombre}: {p.descripcion}")
    eleccion = int(input("\nSelecciona el número de tu personaje: ")) - 1
    return opciones[eleccion]

def batalla(jugador, enemigo):
    print(f"\nHas elegido a {jugador.nombre}: {jugador.descripcion}")
    print(f"\nTu enemigo será: {enemigo.nombre}.\n")

    while jugador.vida > 0 and enemigo.vida > 0:
        print(f"\n--- {jugador.nombre} vs {enemigo.nombre} ---")
        print(f"Vida de {jugador.nombre}: {jugador.vida}")
        print(f"Vida de {enemigo.nombre}: {enemigo.vida}\n")

        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Defender")
        accion_jugador = int(input("Selecciona una opción: "))

        defensa_jugador = 0
        defensa_enemigo = 0
        dano_jugador = 0
        dano_enemigo = 0

        if accion_jugador == 1:
            print("Selecciona tu ataque:")
            for i, a in enumerate(jugador.ataques):
                print(f"{i + 1}. {a[0]} (Daño: {a[1]})")
            eleccion = int(input("Número de ataque: ")) - 1
            ataque = jugador.ataques[eleccion]
            dano_jugador = ataque[1]
        else:
            print("Selecciona tu defensa:")
            for i, d in enumerate(jugador.defensas):
                print(f"{i + 1}. {d[0]} (Protección: {d[1]})")
            eleccion = int(input("Número de defensa: ")) - 1
            defensa = jugador.defensas[eleccion]
            defensa_jugador = defensa[1]
            print(f"{jugador.nombre} se defiende con {defensa[0]}.")

        accion_enemigo = random.choice([1, 2])
        if accion_enemigo == 1:
            ataque = enemigo.atacar()
            dano_enemigo = ataque[1]
            if accion_jugador == 2:
                dano_enemigo -= defensa_jugador
                dano_enemigo = max(0, dano_enemigo)
            jugador.vida -= dano_enemigo
            print(f"{enemigo.nombre} ataca con {ataque[0]} y causa {dano_enemigo} puntos de daño.")
        else:
            defensa = enemigo.defender()
            defensa_enemigo = defensa[1]
            print(f"{enemigo.nombre} se defiende con {defensa[0]}.")

        if accion_jugador == 1:
            dano_jugador -= defensa_enemigo
            dano_jugador = max(0, dano_jugador)
            enemigo.vida -= dano_jugador
            print(f"{jugador.nombre} ataca con {jugador.ataques[eleccion][0]} y causa {dano_jugador} puntos de daño.")

        if jugador.vida <= 0:
            print(f"\n{jugador.nombre} ha sido derrotado. {enemigo.nombre} gana.")
            break
        elif enemigo.vida <= 0:
            print(f"\n{enemigo.nombre} ha sido derrotado. ¡{jugador.nombre} gana!")
            break

# Ejecutar juego
jugador = seleccionar_personaje()
enemigo = random.choice(enemigos)
batalla(jugador, enemigo)
