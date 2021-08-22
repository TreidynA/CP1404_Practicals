MIN_LENGTH = 2
def main():
    password = get_password()
    password_to_astericks(password)


def password_to_astericks(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print('Invalid Password!')
        password = input("Password: ")
    return password


main()