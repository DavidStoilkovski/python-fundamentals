import sys

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def small(num_1, num_2, num_3):
    smallest_of_all = sys.maxsize
    if num_1 <= smallest_of_all:
        smallest_of_all = num_1
    if num_2 <= smallest_of_all:
        smallest_of_all = num_2
    if num_3 <= smallest_of_all:
        smallest_of_all = num_3

    result = smallest_of_all
    return result

result = small(num_1, num_2, num_3)

print(result)