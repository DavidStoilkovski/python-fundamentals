list_numbers = input().split(", ")

group = 10
while len(list_numbers) > 0:
    temp = []
    temp = [int(num) for num in list_numbers if int(num) <= group]
    for num in temp:
        list_numbers.remove(str(num))
    print(f"Group of {group}'s: {temp}")
    group += 10