import random
ORANGE = "\033[38;5;208m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
POKEMON_LIST = [
    {
        "name": "Charmander",
        "type": "Fire",
        "color": ORANGE,
        "hp": 100,
        "attack": 30,
        "defense": 20,
        "normal_move": "Scratch",
        "type_move": "Ember"
    },
    {
        "name": "Squirtle",
        "type": "Water",
        "color": CYAN,
        "hp": 100,
        "attack": 30,
        "defense": 20,
        "normal_move": "Tackle",
        "type_move": "Water Gun"
    },
    {
        "name": "Bulbasaur",
        "type": "Grass",
        "color": GREEN,
        "hp": 100,
        "attack": 30,
        "defense": 20,
        "normal_move": "Headbutt",
        "type_move": "Vine Whip"
    }
]

def type_multiplier(attack_type, defend_type):
    if attack_type == "Fire" and defend_type == "Grass":
        return 2.0
    if attack_type == "Grass" and defend_type == "Water":
        return 2.0
    if attack_type == "Water" and defend_type == "Fire":
        return 2.0
    if attack_type == defend_type:
        return 1.0
    else:
        return 0.5

def calculate_damage(attacker, defender, move_type):
    if move_type == "normal":
        base = 20
        multiplier = 1.0
    else:
        base = 30
        multiplier = type_multiplier(attacker["type"], defender["type"])

    damage = (base + attacker["attack"] - defender["defense"]) * multiplier
    return max(1, int(damage))

def choose_player_pokemon():
    print("Choose your Pokémon to defeat your Rival:")
    for i, p in enumerate(POKEMON_LIST, start=1):
        # We wrap the name in the color code and the reset code
        print(f"{i}. {p['color']}{p['name']}{RESET} ({p['type']})")

    while True:
        choice = input("Enter number: ")
        if choice in ("1", "2", "3"):
            return POKEMON_LIST[int(choice) - 1]
        print("Invalid choice.")

def choose_cpu_pokemon(player_pokemon):
    remaining = [p for p in POKEMON_LIST if p != player_pokemon]
    return random.choice(remaining)

def battle(player, cpu):
    print(f"\nBattle Start!")
    print(f"You chose {player['color']}{player['name']}{RESET}")
    print(f"Rival chose {cpu['color']}{cpu['name']}{RESET}\n")

    while player["hp"] > 0 and cpu["hp"] > 0:
        print(f"Your pokemon's HP: {player['hp']} | Rival pokemon's HP: {cpu['hp']}")
        print("Choose your move:")
        print(f"1. {player['normal_move']} (Normal)")
        print(f"2. {player['color']}{player['type_move']}{RESET} ({player['type']})")

        move = input("Enter 1 or 2: ")
        if move == "1":
            damage = calculate_damage(player, cpu, "normal")
            print(f"You used {player['normal_move']}!")
        elif move == "2":
            damage = calculate_damage(player, cpu, "type")
            print(f"You used {player['color']}{player['type_move']}{RESET}!")
        else:
            print("Invalid move. Turn skipped.")
            continue

        cpu["hp"] -= damage
        print(f"It dealt {damage} damage!")

        if cpu["hp"] <= 0:
            print(f"\n{cpu['color']}{cpu['name']}{RESET} fainted. You win!")
            break

        cpu_move = random.choice(["normal", "type"])
        if cpu_move == "normal":
            damage = calculate_damage(cpu, player, "normal")
            print(f"Rival used {cpu['normal_move']}!")
        else:
            damage = calculate_damage(cpu, player, "type")
            print(f"Rival used {cpu['color']}{cpu['type_move']}{RESET}!")

        player["hp"] -= damage
        print(f"It dealt {damage} damage!\n")

        if player["hp"] <= 0:
            print(f"\n{player['color']}{player['name']}{RESET} fainted. Rival wins!")
            break

player_pokemon = choose_player_pokemon()
cpu_pokemon = choose_cpu_pokemon(player_pokemon)
player_pokemon = player_pokemon.copy()
cpu_pokemon = cpu_pokemon.copy()
battle(player_pokemon, cpu_pokemon)
