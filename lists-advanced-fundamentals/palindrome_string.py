list_words = input().split()
searched_word = input()

list_words = [word for word in list_words if word[::-1] == word]
count = [word for word in list_words if word == searched_word]

print(list_words)
print(f"Found palindrome {len(count)} times")