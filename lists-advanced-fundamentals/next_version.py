version = input().split(".")

for ver in range(len(version) - 1, -1, -1):
    current = int(version[ver])
    if current < 9:
        current += 1
        version[ver] = str(current)
        break
    else:
        current = 0
        version[ver] = str(current)

version = ".".join(version)
print(version)
