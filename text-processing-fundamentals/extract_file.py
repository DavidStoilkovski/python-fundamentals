file_path = input()

file_path = file_path.split("\\")

file = file_path[-1].split(".")

file_name = file[0]
file_type = file[1]

print(f"File name: {file_name}")
print(f"File extension: {file_type}")
