list_string = input()
list_string = list_string.split(", ")
beggars = int(input())

my_list = []
result = 0

for i in range(beggars):

    for k in range(i, len(list_string), beggars):
        result += int(list_string[k])

    my_list.append(result)
    result = 0

print(my_list)
