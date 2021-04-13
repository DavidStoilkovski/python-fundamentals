import re
loop = int(input())

pattern = r"^[@]#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for i in range(loop):
    barcode = input()

    if bool(re.match(pattern, barcode)):
        group_number = ""
        for i in range(len(barcode)):
            if barcode[i].isdigit():
                group_number += barcode[i]
        if group_number == "":
            print(f"Product group: 00")
        else:
            group_number = int(group_number)
            print(f"Product group: {group_number}")
    else:
        print("Invalid barcode")