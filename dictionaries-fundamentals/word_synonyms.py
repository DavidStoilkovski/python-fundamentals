loop_count = int(input())

dictionary = {}

for _ in range(loop_count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = synonym
    else:
        dictionary[word] +=", " + synonym

for el in dictionary:
    print(f"{el} - {dictionary[el]}")

