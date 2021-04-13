num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def add_and_substract(num_1, num_2, num_3):
    result = num_1 + num_2
    result -= num_3
    return result

result = add_and_substract(num_1, num_2, num_3)
print(result)