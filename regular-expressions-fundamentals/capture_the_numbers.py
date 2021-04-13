import re

text = input()

while text:

    pattern = r"(\d+)"

    result = re.finditer(pattern, text)

    for number in result:
        print(number.group(), end=" ")

    text = input()