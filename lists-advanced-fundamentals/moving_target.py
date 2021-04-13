target_list = input().split()
command = input()

while not command == "End":
    what, where, how = command.split()

    if what == "Shoot":
        if len(target_list) >= int(where) >= 0:
            target_list[int(where)] = int(target_list[int(where)]) - int(how)
            if int(target_list[int(where)]) <= 0:
                target_list.remove(target_list[int(where)])
            else:
                target_list[int(where)] = str(target_list[int(where)])

    elif what == "Add":
        if len(target_list) > int(where) >= 0:
            target_list.insert(int(where), how)
        else:
            print("Invalid placement!")

    elif what == "Strike":
        first = int(where) - int(how)
        last = int(where) + int(how)
        if first >= 0:
            if len(target_list) >= last:
                for delete in range(first, last + 1):
                    target_list.remove(target_list[first])
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")

    command = input()

target_list = "|".join(target_list)
print(target_list)