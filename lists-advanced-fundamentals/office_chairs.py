rooms = int(input())

game_on = True
free_chairs = 0

for room in range(1, rooms + 1):
    actual_taken_list = input().split()
    actual = actual_taken_list[0]
    taken = actual_taken_list[1]

    if len(actual) < int(taken):
        print(f'{int(taken) - len(actual)} more chairs needed in room {room}')
        game_on = False
    else:
        free_chairs += len(actual) - int(taken)

if game_on:
    print(f'Game On, {free_chairs} free chairs left')