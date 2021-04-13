fire_list = input()
fire_list = fire_list.split("#")
water = int(input())

effort = 0

high_fire = range(81, 126)
medium_fire = range(51, 81)
low_fire = range(1, 51)

put_out_cells = []

for fire in fire_list:
    fire = fire.split(" = ")
    fire_type = fire[0]
    fire_range = int(fire[1])

    if fire_type == "High" and not fire_range in high_fire:
        continue
    if fire_type == "Medium" and not fire_range in medium_fire:
        continue
    if fire_type == "Low" and not fire_range in low_fire:
        continue

    if water >= fire_range:
        put_out_cells.append(fire_range)
        effort += fire_range * 0.25
        water -= fire_range

print("Cells:")

for cell in put_out_cells:
    print(f" - {cell}")

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(put_out_cells)}')
