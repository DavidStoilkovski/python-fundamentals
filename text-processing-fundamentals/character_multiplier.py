string = input().split()

string_1 = string[0]
string_2 = string[1]

sum = 0

if len(string_1) == len(string_2):
    for i in range(len(string_1)):
        sum += (ord(string_1[i]) * ord(string_2[i]))
    print(sum)
    exit(0)

if len(string_1) < len(string_2):
    shorter = string_1
    longer = string_2
else:
    shorter = string_2
    longer = string_1

for i in range(len(shorter)):
    sum += (ord(string_1[i]) * ord(string_2[i]))

for i in range(len(shorter), len(longer)):
    sum += ord(longer[i])

print(sum)
