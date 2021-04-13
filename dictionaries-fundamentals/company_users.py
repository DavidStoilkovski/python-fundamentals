line = input()

companies_dict = {}

while not line == "End":
    line = line.split(" -> ")
    company = line[0]
    user = line[1]

    if company not in companies_dict:
        users = []
        users.append(user)
        companies_dict[company] = users
    else:
        if user not in companies_dict[company]:
            companies_dict[company].append(user)

    line = input()

companies_dict = dict(sorted(companies_dict.items(), key=lambda x: x[0]))

for company in companies_dict:
    print(company)
    for user in companies_dict[company]:
        print(f'-- {user}')
