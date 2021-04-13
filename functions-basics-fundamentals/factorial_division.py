def factorial_division(num_1, num_2):
    factorial_1 = 1
    for number_1 in range(2, num_1 + 1):
        factorial_1 *= number_1
    factorial_2 = 1
    for number_2 in range(2, num_2 + 1):
        factorial_2 *= number_2
    result = factorial_1 / factorial_2
    return result

num_1 = int(input())
num_2 = int(input())

result = factorial_division(num_1, num_2)
print(f'{result:.2f}')