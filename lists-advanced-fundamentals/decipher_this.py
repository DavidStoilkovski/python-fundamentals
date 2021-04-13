messages = input().split()

new_message = []

for message in messages:
    temp = []
    for letter in message:
        if letter.isnumeric():
            temp.append(letter)
    temp = "".join(temp)
    our_letter = chr(int(temp))
    message = message.replace(temp, our_letter)
    new_message.append(message)

for word in new_message:
    if len(word) > 2:
        word = word[0] + word[-1:] + word[2:-1] + word[1:2]
        print(word, end=" ")
    else:
        print(word, end=" ")