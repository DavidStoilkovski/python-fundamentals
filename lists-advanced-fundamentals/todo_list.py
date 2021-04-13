command = input()

todo_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while not command == "End":
    command = command.split("-")
    position = int(command[0])
    task = command[1]
    todo_list.insert(position, task)
    command = input()
result = []
for element in todo_list:
    if not element == 0:
        result.append(element)

print(result)