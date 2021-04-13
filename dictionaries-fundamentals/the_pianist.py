loop = int(input())

songs = {}

for _ in range(loop):
    line = input().split("|")

    each = []

    each.append(line[1])
    each.append(line[2])

    songs[line[0]] = each

line = input()

while not line == "Stop":

    line = line.split("|")

    command = line[0]

    if command == "Add":

        piece = line[1]
        composer = line[2]
        key = line[3]

        if piece not in songs:
            each = []
            each.append(composer)
            each.append(key)
            songs[piece] = each
            print(f"{piece} by {composer} in {key} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    elif command == "Remove":

        piece = line[1]

        if piece in songs:
            del songs[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":

        piece = line[1]
        key = line[2]

        if piece in songs:
            songs[piece][1] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    line = input()

songs = dict(sorted(songs.items(), key=lambda x: (x[0], x[1][0],)))

for every in songs:
    piece = every
    composer = songs[every][0]
    key = songs[every][1]

    print(f"{every} -> Composer: {composer}, Key: {key}")