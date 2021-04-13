input_list = input()

input_list = input_list.split(" ")
inverted_list = []

for number in input_list:
    number = int(number)
    number *= -1
    inverted_list.append(number)

print(inverted_list)