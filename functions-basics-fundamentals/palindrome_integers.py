def palindrome(number):
    number = number.split(', ')
    for i in range(len(number)):
        temp = str(number[i])
        reversed_number = ''
        for k in range(len(temp) -1, -1, -1):
            reversed_number += temp[k]
        reversed_number = int(reversed_number)
        temp = int(temp)
        if temp == reversed_number:
            statement.append('True')
        else:
            statement.append('False')
    return statement


statement = []

number = input()
statement = palindrome(number)

for each in range(len(statement)):
    print(statement[each])

