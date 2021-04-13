def odd_and_even_sum(number):
    even = 0
    odd = 0
    filtered = []
    for i in range(len(number)):
        k = int(number[i])
        if k % 2 == 0:
            even += k
        else:
            odd += k

    filtered.append(even)
    filtered.append(odd)
    return filtered

number = input()
filtered = odd_and_even_sum(number)
even_sum = filtered[0]
odd_sum = filtered[1]

print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')