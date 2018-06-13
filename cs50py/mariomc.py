import cs50

while True:
    print("Height: ", end="")
    height = cs50.get_int()
    if (height >= 0 and height <= 23):
        break
for i in range(height):

    spaces = height - 1 - i
    for j in range(spaces):
        print(" ", end="")

    for j in range(i + 1):
        print("#", end="")

    print("  ", end="")

    for j in range(i + 1):
        print("#", end="")
    print()