def repeat_string(text, repeat):
    result = ""
    for i in range(repeat):
        result += text
    return result

text = input()
repeat = int(input())
result = repeat_string(text, repeat)
print(result)