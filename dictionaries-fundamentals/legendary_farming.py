loop = True

key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
key_materials_list = ['shards', 'fragments', 'motes']
junk = {}

while loop:
    line = input().split()
    for i in range(0, len(line), 2):
        component = line[i+1].lower()

        if component in key_materials_list:
            key_materials[component] += int(line[i])

            if key_materials[component] >= 250:
                loop = False
                break

        else:
            if component not in junk:
                junk[component] = int(line[i])
            else:
                junk[component] += int(line[i])

for el in key_materials:
    if el == "shards" and key_materials[el] >= 250:
        key_materials[el] -= 250
        print('Shadowmourne obtained!')
    elif el == "fragments" and key_materials[el] >= 250:
        key_materials[el] -= 250
        print('Valanyr obtained!')
    elif el == "motes" and key_materials[el] >= 250:
        key_materials[el] -= 250
        print('Dragonwrath obtained!')


key_materials = dict(sorted(key_materials.items(), key=lambda x: x[0]))
key_materials = dict(sorted(key_materials.items(), key=lambda x: x[1], reverse = True))

for el in key_materials:
    print(f'{el}: {key_materials[el]}')

junk = dict(sorted(junk.items(), key=lambda x: x[0]))


for el in junk:
    print(f'{el}: {junk[el]}')