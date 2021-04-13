loop = int(input())

heroes_dict = {}

for i in range(loop):

    points_dict = {}

    line = input().split()

    hero = line[0]
    hp = int(line[1])
    mp = int(line[2])

    points_dict["hp"] = hp
    points_dict["mp"] = mp

    if hero in heroes_dict:
        heroes_dict[hero]['hp'] += hp
        heroes_dict[hero]['mp'] += mp
    else:
        heroes_dict[hero] = points_dict

    if heroes_dict[hero]["hp"] > 100:
        heroes_dict[hero]["hp"] = 100

    if heroes_dict[hero]["mp"] > 200:
        heroes_dict[hero]["mp"] = 200

line = input()

while not line == "End":

    line = line.split(" - ")

    command = line[0]
    hero = line[1]

    if command == "CastSpell":

        mp_needed = int(line[2])
        spell_name = line[3]

        if heroes_dict[hero]["mp"] >= mp_needed:
            heroes_dict[hero]["mp"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":

        damage = int(line[2])
        attacker = line[3]

        heroes_dict[hero]["hp"] -= damage

        if heroes_dict[hero]["hp"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero]['hp']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes_dict[hero]

    elif command == "Recharge":

        amount = int(line[2])

        if heroes_dict[hero]['mp'] + amount > 200:
            print(f"{hero} recharged for {(200 - heroes_dict[hero]['mp']):.0f} MP!")
            heroes_dict[hero]['mp'] = 200
        else:
            print(f"{hero} recharged for {amount} MP!")
            heroes_dict[hero]['mp'] += amount

    elif command == "Heal":

        amount = int(line[2])

        if heroes_dict[hero]['hp'] + amount > 100:
            print(f"{hero} healed for {(100 - heroes_dict[hero]['hp']):.0f} HP!")
            heroes_dict[hero]['hp'] = 100
        else:
            print(f"{hero} healed for {amount} HP!")
            heroes_dict[hero]['hp'] += amount

    line = input()

heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1]['hp'], x[0])))

for hero in heroes_dict:
    print(hero)
    print(f"  HP: {heroes_dict[hero]['hp']}")
    print(f"  MP: {heroes_dict[hero]['mp']}")
