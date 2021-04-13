list_of_numbers = input().split(", ")

even_numbers_list = [index for index in range(len(list_of_numbers)) if int(list_of_numbers[index]) % 2 == 0]

print(even_numbers_list)