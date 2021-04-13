message = input()

line  = input()

while not line == "Reveal":
    line = line.split(":|:")

    command = line[0]

    if command == "InsertSpace":
        index = int(line[1])
        message = message[:index] + " " + message[index::]
        print(message)

    elif command == "Reverse":
        substring = line[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            add = substring[::-1]
            message = message + add
            print(message)
        else:
            print("error")

    elif command == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        message = message.replace(substring, replacement)
        print(message)

    line = input()

print(f"You have a new text message: {message}")