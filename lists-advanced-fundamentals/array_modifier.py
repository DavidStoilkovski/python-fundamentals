list_with_elements = input().split()
list_with_elements = [int(el) for el in list_with_elements]

while True:

    user_input = input()
    if user_input == "end":
        break
    user_input = user_input.split()
    command = user_input[0]

    if command == "swap":
        first_element = int(user_input[1])
        second_element = int(user_input[2])
        list_with_elements[first_element], list_with_elements[second_element] = list_with_elements[second_element], list_with_elements[first_element]
    elif command == "multiply":
        first_element = int(user_input[1])
        second_element = int(user_input[2])
        list_with_elements[first_element] = list_with_elements[first_element] * list_with_elements[second_element]
    elif command == "decrease":
        list_with_elements = [(el-1) for el in list_with_elements]


list_with_elements = [str(el) for el in list_with_elements]
print(", ".join(list_with_elements))