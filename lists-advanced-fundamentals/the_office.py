happiness_list = input().split()
happiness_multiply = int(input())

multiplied_happiness_list = []

for every in happiness_list:
    multiplied_happiness_list.append(int(every) * happiness_multiply)

border = sum(multiplied_happiness_list) / len(multiplied_happiness_list)

happy_employees = [employee for employee in multiplied_happiness_list if int(employee) >= border]

if len(happy_employees) >= (len(multiplied_happiness_list) / 2):
    print(f'Score: {len(happy_employees)}/{len(multiplied_happiness_list)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(multiplied_happiness_list)}. Employees are not happy!')