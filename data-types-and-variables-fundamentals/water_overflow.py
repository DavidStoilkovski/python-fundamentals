tank = 255

n = int(input())

total = 0

for i in range(n):
    i = float(input())
    if total + i > tank:
        print("Insufficient capacity!")
    else:
        total += i

print(f'{total:.0f}')