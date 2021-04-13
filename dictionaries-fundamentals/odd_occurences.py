words = input().split()

dictionary = {}

for word in words:
    word = word.lower()
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

for word in dictionary:
    if not dictionary[word] % 2 == 0:
        print(word, end=" ")