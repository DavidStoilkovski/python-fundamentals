import re

text = input()
pattern = r"\b\_([A-Za-z0-9]+\b)"
matches = []

result = re.finditer(pattern, text)

for match in result:
    matches.append(match.group(1))

print(",".join(matches))