houses_list = input().split("@")
houses_list = [int(el) for el in houses_list]

jump_places = 0
command = input()

while not command == "Love!":
    command = command.split()
    jump_places += int(command[1])

    if jump_places < len(houses_list):
        if houses_list[jump_places] == 0:
            print(f"Place {jump_places} already had Valentine's day.")
        else:
            houses_list[jump_places] -= 2
            if houses_list[jump_places] == 0:
                print(f"Place {jump_places} has Valentine's day.")
    else:
        jump_places = 0
        if houses_list[jump_places] == 0:
            print(f"Place {jump_places} already had Valentine's day.")
        else:
            houses_list[jump_places] -= 2
            if houses_list[jump_places] == 0:
                print(f"Place {jump_places} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {jump_places}.")

if sum(houses_list) == 0:
    print("Mission was successful.")
else:
    houses_list = [el for el in houses_list if not el == 0]
    print(f"Cupid has failed {len(houses_list)} places.")