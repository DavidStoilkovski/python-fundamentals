loop = int(input())

cars_dict = {}

for _ in range(loop):
    line = input().split("|")

    mile_fuel_dict = {}

    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])

    mile_fuel_dict["Mileage"] = mileage
    mile_fuel_dict["Fuel"] = fuel

    cars_dict[car] = mile_fuel_dict

line = input()

while not line == "Stop":
    line = line.split(" : ")

    command = line[0]

    if command == "Drive":
        car = line[1]
        distance = int(line[2])
        fuel = int(line[3])

        if cars_dict[car]["Fuel"] >= fuel:
            cars_dict[car]["Fuel"] -= fuel
            cars_dict[car]["Mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if cars_dict[car]["Mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars_dict[car]

    elif command == "Refuel":
        car = line[1]
        fuel = int(line[2])

        if fuel + cars_dict[car]["Fuel"] > 75:
            filled_fuel = 75 - cars_dict[car]["Fuel"]
            cars_dict[car]["Fuel"] = 75
        else:
            filled_fuel = fuel
            cars_dict[car]["Fuel"] += fuel

        print(f"{car} refueled with {filled_fuel} liters")

    elif command == "Revert":

        car = line[1]
        mileage = int(line[2])

        if cars_dict[car]["Mileage"] - mileage < 10000:
            cars_dict[car]["Mileage"] = 10000
        else:
            cars_dict[car]["Mileage"] -= mileage
            print(f"{car} mileage decreased by {mileage} kilometers")

    line = input()

cars_dict = dict(sorted(cars_dict.items(), key=lambda x: (-x[1]['Mileage'], x[0])))

for car in cars_dict:
    print(f"{car} -> Mileage: {cars_dict[car]['Mileage']} kms, Fuel in the tank: {cars_dict[car]['Fuel']} lt.")