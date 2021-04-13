# import re
#
# username = input().split(", ")
#
# for i in range(len(username)):
#     if (re.match("^[A-Za-z0-9_-]*$", username[i])) and 3 <= len(username[i]) <= 16:
#         print(username[i])
#

username = input().split(", ")

for i in range(len(username)):
    word = username[i]
    for k in range(len(word)):
        if word[k].isdigit():
            if word[k] == "-" or word[k] == "_":
                print(word[k])
        elif word[k].isalpha():
                print(word[k])