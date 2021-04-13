text = input()

if not text == "":
    result = text[0]


for i in range(1, len(text)):
    previous = text[i-1]

    if not text[i] == previous:
        result += text[i]

if not text == "":
    print(result)