from random import choice
import string
import sys  # if you are calling this script from a CLI


def password_generator(size):
    password_size = int(size)  # number of characters

    values = string.ascii_letters + string.digits + string.punctuation

    password = ''

    for i in range(password_size):
        password += choice(values)

    print(f"Your new password: {password}")


if __name__ == '__main__':
    password_generator(sys.argv[1])
