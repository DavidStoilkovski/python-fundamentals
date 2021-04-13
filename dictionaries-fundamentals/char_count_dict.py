word = input()

dictionary = {}

for i in range(len(word)):
    if word[i] == " ":
        pass
    elif word[i] not in dictionary:
        dictionary[word[i]] = 1
    else:
        dictionary[word[i]] += 1

for char in dictionary:
    print(f"{char} -> {dictionary[char]}")