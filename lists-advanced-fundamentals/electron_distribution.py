total_electrons = int(input())

print_list = []
index = 1

while total_electrons > 0:
    shell_size = 2 * index**2
    if shell_size >= total_electrons:
        print_list.append(total_electrons)
        break
    else:
        print_list.append(shell_size)
        total_electrons -= shell_size
    index += 1

print(print_list)