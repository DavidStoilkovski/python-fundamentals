word = input()

dictionary = {}


while not word == "stop":
    quantity = int(input())

    if word not in dictionary:
        dictionary[word] = quantity
    else:
        dictionary[word] += quantity

    word = input()

for char in dictionary:
    print(f"{char} -> {dictionary[char]}")

