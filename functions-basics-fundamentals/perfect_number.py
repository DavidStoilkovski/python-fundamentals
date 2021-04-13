def perfect_number(number):
    is_valid = False
    list_with_divisors = []
    for index in range(1, number):
        if number % index == 0:
            list_with_divisors.append(index)
    if sum(list_with_divisors) == number:
        is_valid = True
    return is_valid

number = int(input())

if perfect_number(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")