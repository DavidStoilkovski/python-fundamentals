def character_in_range(letter_1, letter_2):
    start = int(ord(letter_1)) + 1
    end = int(ord(letter_2))
    symbols = ''

    if start > end:
        k = start
        start = end + 1
        end = k - 1

    for i in range(start, end):
        symbols += chr(i)
        symbols += ' '

    return symbols

letter_1 = input()
letter_2 = input()

symbols = character_in_range(letter_1, letter_2)
print(symbols)