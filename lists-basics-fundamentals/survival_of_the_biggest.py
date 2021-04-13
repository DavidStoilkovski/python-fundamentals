import sys
my_input = input()
my_input = my_input.split()
n = int(input())

smallest = sys.maxsize
new_list = []

for i in range(n):
    for j in range(int(len(my_input))):
        if int(my_input[j]) < smallest:
            smallest = int(my_input[j])

    my_input.remove(str(smallest))
    smallest = sys.maxsize

for i in range(int(len(my_input))):
    new_list.append(int(my_input[i]))

print(new_list)
