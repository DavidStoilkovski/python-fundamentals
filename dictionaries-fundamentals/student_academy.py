loop = int(input())

academy_dict = {}

for _ in range(loop):
    student = input()
    grade = float(input())

    if student in academy_dict:
        grade += academy_dict[student]
        grade /= 2
        academy_dict[student] = grade
    else:
        academy_dict[student] = grade

academy_dict = dict(sorted(academy_dict.items(), key=lambda x: x[1], reverse=True))

for student in academy_dict:
    if academy_dict[student] >= 4.50:
        print(f'{student} -> {(academy_dict[student]):.2f}')


