persons = int(input())
capacity = int(input())

if persons <= capacity:
    print('All the persons fit inside the elevator.')
    print('Only one course is needed.')
else:
    courses = persons // capacity
    if (persons / capacity) - courses > 0:
        courses += 1
    print(courses)