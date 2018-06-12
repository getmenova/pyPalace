import cs50
while True:
    print("Height: ", end="")
    height = cs50.get_int()
    if height in range(24):
        break
width = height + 1
for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 2), end="")
    print()