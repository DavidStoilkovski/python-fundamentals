line = input()

products_dict = {}

while not line == "statistics":
    line = line.split(": ")
    product = line[0]
    quantity = int(line[1])

    if product not in products_dict:
        products_dict[product] = quantity
    else:
        products_dict[product] += quantity

    line = input()

print("Products in stock:")
for product in products_dict:
    print(f"- {product}: {products_dict[product]}")

print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {sum(products_dict.values())}")