line = input()

data_dict = {}

while not line == "Sail":
    line = line.split("||")

    city = line[0]
    population = int(line[1])
    gold = int(line[2])

    if city in data_dict:
        data_dict[city]['population'] += population
        data_dict[city]['gold'] += gold
    else:
        data_dict[city] = {'population': population, 'gold': gold}

    line = input()

data_line = input()

while not data_line == "End":

    data_line = data_line.split("=>")

    command = data_line[0]

    if command == "Plunder":
        town = data_line[1]
        people = int(data_line[2])
        gold = int(data_line[3])

        data_dict[town]['population'] -= people
        data_dict[town]['gold'] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if data_dict[town]['population'] <= 0 or data_dict[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del data_dict[town]

    elif command == "Prosper":
        town = data_line[1]
        gold = int(data_line[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            data_dict[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {data_dict[town]['gold']} gold.")

    data_line = input()

data_dict = dict(sorted(data_dict.items(), key=lambda x: (-x[1]['gold'], x[0])))

if data_dict:
    print(f"Ahoy, Captain! There are {len(data_dict)} wealthy settlements to go to:")

    for town in data_dict:
        print(f"{town} -> Population: {data_dict[town]['population']} citizens, Gold: {data_dict[town]['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")