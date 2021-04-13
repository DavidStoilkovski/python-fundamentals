list_elements = int(input())

trains_list =[]

for elements in range(list_elements):
    trains_list.append(0)

command = input()


while not command == "End":
    command = command.split()
    if command[0] == "add":
        trains_list[-1] += int(command[1])
    elif command[0] == "insert":
        trains_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        trains_list[int(command[1])] -= int(command[2])
    command = input()

print(trains_list)