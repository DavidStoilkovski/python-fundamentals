number = int(input())

start = 97
end = start + number

for i in range(start, end):
    for j in range(start, end):
        for k in range(start, end):
            print(f'{chr(i)}{chr(j)}{chr(k)}')