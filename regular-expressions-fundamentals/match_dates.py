import re

text = input()

pattern = r"(?P<day>\d{2})(?P<separator>[/.-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

result = re.finditer(pattern, text)

for date in result:
    d = date.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")
