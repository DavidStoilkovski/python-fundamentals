line = input()

digits = ""
letters = ""
others = ""

for el in line:
    if el.isalpha():
        letters += el
    elif el.isdigit():
        digits += el
    else:
        others += el

print(digits)
print(letters)
print(others)