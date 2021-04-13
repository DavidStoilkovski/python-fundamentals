string = input()

line = input()

while not line == "Travel":
    line = line.split(":")

    command = line[0]

    if command == "Add Stop":
        start_index = int(line[1])
        if start_index in range(0, len(string)):
            add_string = line[2]
            string = string[:start_index] + add_string + string[start_index::]

    elif command == "Remove Stop":
        start_index = int(line[1])
        if start_index in range(0, len(string)):
            end_index = int(line[2]) + 1
            if end_index > start_index and end_index in range(0, len(string)+1):
                string = string[:start_index] + string[end_index::]

    elif command == "Switch":
        old_string = line[1]
        new_string = line[2]

        if old_string in string:
            string = string.replace(old_string, new_string)

    print(string)
    line = input()

print(f"Ready for world tour! Planned stops: {string}")