list_with_products = input().split("!")

line = input()


while not line == "Go Shopping!":
    line = line.split()
    command = line[0]
    item_1 = line[1]

    if command == "Urgent" and not (item_1 in list_with_products):
        list_with_products.insert(0, item_1)
    elif command == "Unnecessary" and item_1 in list_with_products:
        list_with_products.remove(item_1)
    elif command == "Correct" and item_1 in list_with_products:
        item_2 = line[2]
        list_with_products[list_with_products.index(item_1)] = item_2
    elif command == "Rearrange" and item_1 in list_with_products:
        list_with_products.remove(item_1)
        list_with_products.append(item_1)

    line = input()

print(", ".join(list_with_products))