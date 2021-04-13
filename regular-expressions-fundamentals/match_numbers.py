import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

result = re.finditer(pattern, text)

result = [number.group() for number in result]
print(*result)