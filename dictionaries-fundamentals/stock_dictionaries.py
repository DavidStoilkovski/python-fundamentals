stock_list = input().split()
check_list = input().split()

stock_dictionary = {}
# search_dictionary = {}
 
for i in range(0, len(stock_list), 2):
    key = stock_list[i]
    value = stock_list[i + 1]

    stock_dictionary[key] =  int(value)

# for k in range(0, len(check_list), 2):
#     key = check_list[i]
#     value = check_list[i + 1]

#     search_dictionary[key] =  int(value)
k = 0

for product in check_list:
    if product in stock_dictionary:
        print(f"We have {stock_dictionary[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")