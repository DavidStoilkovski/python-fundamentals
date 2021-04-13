products_list = input()
products_list = products_list.split("|")
budget = int(input())

profit = 0
sell_price_list = []


for product in products_list:
    product = product.split("->")
    type_product = product[0]
    price_of_product = float(product[1])

    if type_product == "Clothes" and price_of_product > 50:
        continue
    if type_product == "Shoes" and price_of_product > 35:
        continue
    if type_product == "Accessories" and price_of_product > 20.50:
        continue

    if budget >= price_of_product:
        profit += price_of_product * 0.4
        sell_price_list.append(price_of_product * 1.40)
        budget -= price_of_product

for sell_price in sell_price_list:
    print(f'{sell_price:.2f}', end=" ")

print()
print(f'Profit: {profit:.2f}')

if (sum(sell_price_list) + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")