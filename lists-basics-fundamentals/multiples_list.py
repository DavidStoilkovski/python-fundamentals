start = int(input())
second_num = int(input())

end = start * second_num

multiples_list = []

for i in range(start, end + 1, start):
    multiples_list.append(i)

print(multiples_list)