import cs50
import sys

# check for input
if not len(sys.argv) == 2:
    print("Usage: {} <key>".format(sys.argv[0]))
    exit(1)

# prompt user for entry
ptxt = input("plaintext: ")
print("ciphertext: ", end="")

# convert chars character by character
for char in ptxt:

    # support uppercase
    if char.isupper():
        print(chr((ord(char) - ord('A') + int(sys.argv[1])) % 26 + ord('A')), end="")

    # support lowercase
    elif char.islower():
        print(chr((ord(char) - ord('a') + int(sys.argv[1])) % 26 + ord('a')), end="")

    # everything else..
    else:
        print(char, end="")
print()