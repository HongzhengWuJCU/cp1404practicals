MINIMUM_LENGTH=8
def main():
    # run the main function
    get_password()


def get_password():
    # Refactor password check program to use functions
    password = input("Input the password: ")
    while len(password) < MINIMUM_LENGTH:
        print("The password is too short")
        password = input("Input the password: ")


main()