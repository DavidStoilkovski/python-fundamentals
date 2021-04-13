n = int(input())
searched_word = input()

list_of_all = []
filtered_list = []

for i in range(n):
    word = input()
    list_of_all.append(word)
    if searched_word in word:
        filtered_list.append(word)

print(list_of_all)
print(filtered_list)
