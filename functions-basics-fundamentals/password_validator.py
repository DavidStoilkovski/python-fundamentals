def pass_validator(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    for element in password:
        if not element.isdigit() and not element.isalpha():
            is_valid = False
            print('Password must consist only of letters and digits')
            break
    count = 0
    for element in password:
        if element.isdigit():
            count += 1
    if count < 2:
        is_valid =  False
        print('Password must have at least 2 digits')

    return is_valid

password = input()

if pass_validator(password):
    print('Password is valid')
