loop = int(input())

plants_dict = {}

for _ in range(loop):
    line = input().split("<->")
    plant = line[0]
    rarity = {}

    rarity['Rarity'] = int(line[1])
    plants_dict[plant] = rarity

line = input()

while not line == "Exhibition":

    try:

        line = line.split(": ")

        command = line[0]

        if command == "Rate":
            line[1] = line[1].split(" - ")

            plant = line[1][0]
            rating = line[1][1]

            find = plants_dict[plant]

            if find.get("Rating"):
                new_value = (plants_dict[plant]['Rating'] + int(rating)) / 2
                plants_dict[plant]['Rating'] = new_value

            else:
                plants_dict[plant]['Rating'] = int(rating)

        elif command == "Update":

            line[1] = line[1].split(" - ")
            plant = line[1][0]
            rarity = line[1][1]

            plants_dict[plant]['Rarity'] = int(rarity)

        elif command == "Reset":
            line[1] = line[1].split(" - ")
            plant = line[1][0]

            plants_dict[plant]['Rating'] = 0

    except:
        print('error')
        exit(0)

    line = input()

plants_dict = dict(sorted(plants_dict.items(), key=lambda x: (-x[1]['Rarity'], -x[1]['Rating'],)))


print("Plants for the exhibition:")
for plant in plants_dict:
    print(f"- {plant}; Rarity: {plants_dict[plant]['Rarity']}; Rating: {plants_dict[plant]['Rating']:.2f}")