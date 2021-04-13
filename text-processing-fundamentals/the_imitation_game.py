crypted_message = input()

line = input()

while not line == "Decode":
    line = line.split("|")

    command = line[0]

    if command == "Move":
        index = int(line[1])
        crypted_message = crypted_message[index::] + crypted_message[:index]

    elif command == "Insert":
        index = int(line[1])
        letter = line[2]

        crypted_message = crypted_message[:(index)] + letter + crypted_message[index::]

    elif command == "ChangeAll":

        old_letter = line[1]
        new_letter = line[2]

        crypted_message = crypted_message.replace(old_letter, new_letter)

    line = input()

print(f"The decrypted message is: {crypted_message}")