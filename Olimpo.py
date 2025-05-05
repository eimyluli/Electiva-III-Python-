import random

# opciones que tiene el jugador como personaje, contiene listas y dentro de ella duplas en los ataques y defensas
personajes = [
    {
        "nombre": "Zeus",
        "descripcion": " Rey de los dioses, dios del cielo y el rayo. ",
        "vida": 100,
        "ataques": [("Rayo celestial", 30), ("Tormenta divina", 20), ("Golpe de trueno", 15)],
        "defensas": [("Escudo de rayos", 20), ("Esquivar", 10)]
    },
    {
        "nombre": "Hera",
        "descripcion": " Reina de los dioses.",
        "vida": 110,
        "ataques": [("Lazo del destino", 25), ("Gracia castigadora", 18), ("Grito de autoridad", 12)],
        "defensas": [("Aura protectora", 18), ("Retroceso místico", 8)]
    },
    {
        "nombre": "Atenea",
        "descripcion": "Diosa de la sabiduría, la guerra estratégica y las artes.",
        "vida": 105,
        "ataques": [("Lanza de sabiduría", 28), ("Táctica implacable", 19), ("Conjuro mental", 14)],
        "defensas": [("Escudo aegis", 22), ("Postura defensiva", 9)]
    }
]

# elección aleatoria del enemigo
enemigos = [
    {
        "nombre": "Némesis",
        "vida": 100,
        "ataques": [("Juicio divino", 25), ("Castigo oscuro", 18), ("Daga equilibrante", 14)],
        "defensas": [("Justicia ciega", 18), ("Esquiva sombría", 9)]
    },
    {
        "nombre": "Minotauro",
        "vida": 120,
        "ataques": [("Embiste brutal", 30), ("Rugido ensordecedor", 20), ("Golpe con hacha", 15)],
        "defensas": [("Piel gruesa", 20), ("Cubrebrazo tosco", 10)]
    },
    {
        "nombre": "Titán Tifón",
        "vida": 130,
        "ataques": [("Tormenta infernal", 35), ("Fuego de montaña", 22), ("Aliento de caos", 18)],
        "defensas": [("Barrera titánica", 25), ("Resistencia salvaje", 12)]
    }
]

# permite elegir el personaje
print("¡Elige tu personaje!\n")
for i, personaje in enumerate(personajes):
    print(f"{i + 1}. {personaje['nombre']}: {personaje['descripcion']}")

eleccion = int(input("\nSelecciona el número de tu personaje: ")) - 1
jugador = personajes[eleccion]

# Mostrar descripción una sola vez
print(f"\nHas elegido a {jugador['nombre']}: {jugador['descripcion']}")

# elección aleatoria del enemigo
enemigo = random.choice(enemigos)
print(f"\nTu enemigo será: {enemigo['nombre']}.\n")

# Inicia la pelea, luego de seleccionar el personaje
while jugador["vida"] > 0 and enemigo["vida"] > 0:
    print(f"\n--- {jugador['nombre']} vs {enemigo['nombre']} ---")
    print(f"Vida de {jugador['nombre']}: {jugador['vida']}")
    print(f"Vida de {enemigo['nombre']}: {enemigo['vida']}\n")

    # el jugador debe elegir entre atacar y defender
    print("¿Qué deseas hacer?")
    print("1. Atacar")
    print("2. Defender")
    accion_jugador = int(input("Selecciona una opción: "))

    defensa_jugador = 0
    defensa_enemigo = 0
    dano_jugador = 0
    dano_enemigo = 0

    # selecciona el tipo de ataque o defensa
    # ATAQUE
    if accion_jugador == 1:  
        print("Selecciona tu ataque:")
        for i, ataque in enumerate(jugador["ataques"]):
            print(f"{i + 1}. {ataque[0]} (Daño: {ataque[1]})")
        eleccion_ataque = int(input("Selecciona el número de tu ataque: ")) - 1
        ataque_jugador = jugador["ataques"][eleccion_ataque]
        dano_jugador = ataque_jugador[1]

    # DEFENSA
    elif accion_jugador == 2:  
        print("Selecciona tu defensa:")
        for i, defensa in enumerate(jugador["defensas"]):
            print(f"{i + 1}. {defensa[0]} (Protección: {defensa[1]})")
        eleccion_defensa = int(input("Selecciona el número de tu defensa: ")) - 1
        defensa_jugador = jugador["defensas"][eleccion_defensa][1]
        print(f"\n{jugador['nombre']} se defiende con {jugador['defensas'][eleccion_defensa][0]}.")

    # Enemigo 1 ataca, 2 defiende 
    accion_enemigo = random.choice([1, 2])  

    # ATAQUE
    if accion_enemigo == 1:  
        ataque_enemigo = random.choice(enemigo["ataques"])
        dano_enemigo = ataque_enemigo[1]

        # Si el jugador se defendió, se reduce el daño
        if accion_jugador == 2:
            dano_enemigo -= defensa_jugador  
            if dano_enemigo < 0:
                dano_enemigo = 0  

        jugador["vida"] -= dano_enemigo
        print(f"\n{enemigo['nombre']} ataca a {jugador['nombre']} con {ataque_enemigo[0]} y causa {dano_enemigo} puntos de daño.")

    # DEFENSA
    elif accion_enemigo == 2:  
        defensa_random = random.choice(enemigo["defensas"])
        defensa_enemigo = defensa_random[1]
        print(f"\n{enemigo['nombre']} se defiende con {defensa_random[0]}.")

    # Aplicar daño del jugador si eligió atacar
    if accion_jugador == 1:
        # Si el enemigo se defendió, se reduce el daño
        dano_jugador -= defensa_enemigo
        if dano_jugador < 0:
            dano_jugador = 0
        enemigo["vida"] -= dano_jugador
        print(f"\n{jugador['nombre']} ataca a {enemigo['nombre']} con {ataque_jugador[0]} y causa {dano_jugador} puntos de daño.")

    # Verifico si perdió o ganó alguno
    if jugador["vida"] <= 0:
        print(f"\n{jugador['nombre']} ha sido derrotado. {enemigo['nombre']} gana.")
        break

    elif enemigo["vida"] <= 0:
        print(f"\n{enemigo['nombre']} ha sido derrotado. ¡{jugador['nombre']} gana!")
        break
