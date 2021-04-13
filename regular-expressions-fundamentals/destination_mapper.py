import re
string = input()

pattern = r"(=|/)([A-Z][A-Za-z]{2,}(\s[A-Z][a-z]{1,})?(\s[A-Z][a-z]{1,})?)\1"

string = re.finditer(pattern, string)

destinations = []
count = 0

for i in string:
    dest = i.group(2)
    if len(dest) >= 3:
        count += len(dest)
        destinations.append(dest)

if count > 0:
    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {count}")
else:
    print(f"Destinations:")
    print(f"Travel Points: 0")

