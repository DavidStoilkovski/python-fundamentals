list_with_numbers = input().split()

list_with_numbers = [int(num) for num in list_with_numbers]

average_number = sum(list_with_numbers) / len(list_with_numbers)

greater_that_average = [num for num in list_with_numbers if num > average_number]

if len(greater_that_average) == 0:
    print('No')
else:
    greater_that_average.sort(reverse=True)
    for i in range(len(greater_that_average)):
        if i > 4:
            break
        print(greater_that_average[i], end=" ")