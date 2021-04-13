key = input()

line = input()

while not line == "Generate":
    line = line.split(">>>")
    command = line[0]

    if command == "Contains":
        substring = line[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print("Substring not found!")
    elif command == "Flip":
        action = line[1]
        start = int(line[2])
        end = int(line[3])
        if action == "Upper":
            original = [key[i] for i in range(start, end)]
            original = "".join(original)
            to_replace = original.upper()
            key = key.replace(original, to_replace)
            print(key)
        else:
            original = [key[i] for i in range(start, end)]
            original = "".join(original)
            to_replace = original.lower()
            key = key.replace(original, to_replace)
            print(key)
    elif command == "Slice":
        start = int(line[1])
        end = int(line[2])
        remove = [key[i] for i in range(start, end)]
        remove = "".join(remove)
        key = key.replace(remove, "")
        print(key)

    line = input()

print(f"Your activation key is: {key}")