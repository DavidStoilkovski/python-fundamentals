line = input()

courses_dict = {}
courses_count = {}

while not line == "end":
    line = line.split(" : ")
    course = line[0]
    user = line[1]

    if course in courses_dict:
        courses_dict[course] += ", " + user
        courses_count[course] += 1
    else:
        courses_dict[course] = user
        courses_count[course] = 1

    line = input()

courses_count = dict(sorted(courses_count.items(), key=lambda x: x[1], reverse=True))

for course in courses_count:
    names = []

    print(f'{course}: {courses_count[course]}')

    courses_dict[course] = courses_dict[course].split(", ")

    for el in courses_dict[course]:
        names.append(el)
    names = sorted(names)

    for name in names:
        print(f'-- {name}')
