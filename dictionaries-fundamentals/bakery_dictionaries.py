bakery_list = input().split()

bakery_dictionary = {}

for i in range(0, len(bakery_list), 2):
    key_index = i
    value_index = i + 1

    key = bakery_list[key_index]
    value = bakery_list[value_index]

    bakery_dictionary[key] = int(value)


print(bakery_dictionary)