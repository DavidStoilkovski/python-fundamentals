cards = input()
cards = cards.split()
shuffles = int(input())

middle = int(len(cards) / 2)

shuffled = []

for i in range(shuffles):
    for j in range(middle):
        shuffled.append(cards[j])
        shuffled.append(cards[middle])
        middle += 1

    middle = int(len(cards) / 2)
    cards = shuffled
    shuffled = []

print(cards)