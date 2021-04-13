event_or_ingredient_list = input()
event_or_ingredient_list = event_or_ingredient_list.split("|")

energy = 100
coins = 100

break_is_true = False

for event in event_or_ingredient_list:
    event = event.split("-")

    case = event[0]
    points = int(event[1])

    if case == "rest":
        previous_energy = energy
        energy += points
        if energy > 100:
            energy = 100
        print(f'You gained {energy - previous_energy} energy.')
        print(f'Current energy: {energy}.')

    elif case == "order":
        if energy - 30 < 0:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += points
            print(f'You earned {points} coins.')

    else:
        if coins - points >= 0:
            coins -= points
            print(f"You bought {case}.")
        else:
            print(f"Closed! Cannot afford {case}.")
            break_is_true = True
            break

if coins >= 0 and break_is_true is False:
    print("Day completed!")
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')