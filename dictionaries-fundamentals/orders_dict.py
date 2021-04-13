line = input()

card = {}
price_quantity = []

while not line == "buy":
    line = line.split()

    item = line[0]
    price = float(line[1])
    quantity = float(line[2])

    if item not in card:
        price_quantity = [price, quantity]
        card[item] = price_quantity
    else:
        quantity += card[item][1]
        price_quantity = [price, quantity]
        card[item] = price_quantity

    line = input()

for item in card:
    print(f"{item} -> {(card[item][0] * card[item][1]):.2f}")