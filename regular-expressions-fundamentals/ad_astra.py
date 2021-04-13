import re

line = input()

pattern = r"(\||#)\w+(\s\w+)?\1\d{2}/\d{2}/\d{2}\1\d+\1"

food = re.finditer(pattern, line)

total_calories = 0

for n in food:
    symbol = n.group(1)
    text = n.group()
    calories = int((n.group()).split(symbol)[3])
    total_calories += calories

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

food = re.finditer(pattern, line)

for i in food:
    symbol = i.group(1)
    text = (i.group()).split(symbol)
    item = text[1]
    best_before = text[2]
    calories = int((i.group()).split(symbol)[3])

    print(f"Item: {item}, Best before: {best_before}, Nutrition: {calories}")
