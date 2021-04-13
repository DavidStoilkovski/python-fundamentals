product = input()
quantity = float(input())

def market(product, quantity):
    if product == "coffee":
        total = 1.50 * quantity
        return total
    elif product == "water":
        total = 1.00 * quantity
        return total
    elif product == "coke":
        total = 1.40 * quantity
        return total
    elif product == "snacks":
        total = 2.00 * quantity
        return total

total = market(product, quantity)
print(f'{total:.2f}')