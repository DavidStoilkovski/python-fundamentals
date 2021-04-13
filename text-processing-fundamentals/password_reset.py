password = input()
line = input()

while not line == "Done":
    line = line.split()
    command = line[0]

    if command == "TakeOdd":
        old_password = password
        password = ""
        for i in range(len(old_password)):
            if not i % 2 == 0:
                password += old_password[i]

        print(password)

    elif command == "Cut":
        start = int(line[1])
        stop = start + int(line[2])
        password = password[:start] + password[stop::]
        print(password)

    elif command == "Substitute":
        substring = line[1]
        substitute = line[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    line = input()

print(f"Your password is: {password}")