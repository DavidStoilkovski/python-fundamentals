import re
text = input()

pattern = r"(\*\*|\:\:)([A-Z][a-z]{2,})\1"

count = 0
valid_emojis = []

cool = re.findall(r"\d", text)
cool_threshold = 1

for number in cool:
    cool_threshold *= int(number)

emojis_found = re.finditer(pattern, text)
emojis = []

for i in emojis_found:
    emoji = i.group(2)
    count += 1
    validator = 0

    for k in range(len(emoji)):
        validator += ord(emoji[k])

    if validator >= cool_threshold:
        emojis.append(i.group(0))

print(f"Cool threshold: {cool_threshold}")
print(f"{count} emojis found in the text. The cool ones are:")
for emoji in emojis:
    print(emoji)