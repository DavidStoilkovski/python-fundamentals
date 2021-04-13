import re

data = input()

pattern = r"^>{2}(?P<product>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"

product = []
total_price = 0

while not data == "Purchase":
    match = re.match(pattern, data)
    if match:
        obj = match.groupdict()
        product.append(obj["product"])
        total_price += float(obj["price"]) * int(obj["quantity"])

    data = input()

print("Bought furniture:")

for el in product:
    print(el)

print(f"Total money spend: {total_price:.2f}")