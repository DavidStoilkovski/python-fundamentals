loop = int(input())

parking = {}

for _ in range(loop):
    line = input().split()

    action = line[0]

    if action == "register":
        user = line[1]
        plates = line[2]
        if user in parking:
            print(f"ERROR: already registered with plate number {plates}")
        else:
            parking[user] = plates
            print(f"{user} registered {plates} successfully")

    elif action == "unregister":
        user = line[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            parking.pop(user)
            print(f"{user} unregistered successfully")

for user in parking:
    print(f"{user} => {parking[user]}")
