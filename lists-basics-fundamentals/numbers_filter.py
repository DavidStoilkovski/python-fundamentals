n = int(input())

list_of_all = []
filtered_list = []


for i in range(n):
    element = input()
    list_of_all.append(element)

magic_word = input()

if magic_word == "even":
    for number in list_of_all:
        number = int(number)
        if number % 2 == 0:
            filtered_list.append(number)
if magic_word == "odd":
    for number in list_of_all:
        number = int(number)
        if not number % 2 == 0:
            filtered_list.append(number)
if magic_word == "negative":
    for number in list_of_all:
        number = int(number)
        if number < 0:
            filtered_list.append(number)
if magic_word == "positive":
    for number in list_of_all:
        number = int(number)
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)