collected_items = input().split(", ")

line = input()

while not line == "Craft!":
    command = line.split(" - ")
    what = command[0]

    if what == "Collect":
        item = command[1]
        if item not in collected_items:
            collected_items.append(item)

    elif what == "Drop":
        item = command[1]
        if item in collected_items:
            collected_items.remove(item)

    elif what == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in collected_items:
            index = collected_items.index(old_item)
            collected_items.insert(index+1, new_item)

    elif what == "Renew":
        item = command[1]
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)

    line = input()

print(", ".join(collected_items))