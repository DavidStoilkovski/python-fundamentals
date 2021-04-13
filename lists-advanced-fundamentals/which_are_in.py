substring_list = input().split(", ")
second_list = input().split(", ")

result = [sub for sub in substring_list for word in second_list if sub in word]

print(sorted(set(result), key=result.index))