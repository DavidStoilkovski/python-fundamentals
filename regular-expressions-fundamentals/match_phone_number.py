import re

text = input()

pattern = r"(\+359-2-\d{3}-\d{4}\b)|(\+359 2 \d{3} \d{4}\b)"

result = re.finditer(pattern, text)
result = [n.group() for n in result]

print(", ".join(result))