import re
text = input()

pattern = r"(@|#)[A-Za-z]{3,}\1{2}\w{3,}"

text = re.finditer(pattern, text)
mirror = 0
pairs = 0

mirror_words = []

for n in text:
    symbol = n.group(1)
    word = n.group().split(symbol)

    if word[1] == word[3][::-1]:
        add = ""
        pairs += 1
        add = word[1] + " <=> " + word[3]
        mirror_words.append(add)

    mirror += 1

if mirror > 0:
    print(f"{mirror} word pairs found!")
else:
    print("No word pairs found!")

if pairs > 0:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")