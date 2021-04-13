not_encrypted = input()

encrypted = ""

for symbol in not_encrypted:

    encrypted_symbol = ord(symbol) + 3
    encrypted_symbol = chr(encrypted_symbol)
    encrypted += encrypted_symbol

print(encrypted)