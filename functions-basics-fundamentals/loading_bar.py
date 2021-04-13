def loading_bar(percent):
    bar = []
    loaded = percent // 10
    for percentage in range(loaded):
        bar.append("%")
    for dot in range(10 - loaded):
        bar.append(".")

    return bar

percent = int(input())

if percent < 100:
    bar = loading_bar(percent)
    print(f"{percent}% [{''.join(bar)}]")
    print('Still loading...')
else:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
