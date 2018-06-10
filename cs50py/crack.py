#brute force import of crack to py

import crypt
import sys

ENCRYPT_LENGTH = 13
SALT_LENGTH = 2

MAX_LENGTH = 5
MIN_SYMBOL = ord(' ')
MAX_SYMBOL = ord('~')

if __name__ == '__main__':
    # make sure the user entered an encrypted password at the command line
    if len(sys.argv) != 2:
        print(f'usage: python {sys.argv[0]} encrypted-string')
        sys.exit(1)

    encrypted = sys.argv[1]


    if len(encrypted) != ENCRYPT_LENGTH:
        print('Invalid encrypted string')
        sys.exit(2)

    alt = encrypted[:SALT_LENGTH]


    guess = bytearray(MAX_LENGTH + 1)
    guess[0] = MIN_SYMBOL


    string_end = 1
    while True:

        encrypted_guess = crypt.crypt(guess[:string_end].decode('ascii'), salt=salt)


        if encrypted == encrypted_guess:
            print(guess.decode('ascii'))
            sys.exit(0)
        idx = 0
        while guess[idx] == MAX_SYMBOL:
            guess[idx] = MIN_SYMBOL
            idx += 1
        if idx == MAX_LENGTH:
            print(f"Couldn't find a password that encrypts to {encrypted}")
            sys.exit(3)
        if guess[idx] == 0:
            string_end += 1
            guess[idx] = MIN_SYMBOL
        else:
            guess[idx] += 1