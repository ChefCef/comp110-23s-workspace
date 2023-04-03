square_to_root: dict[int, int] = {}

i: int = 1
while i < 5:
        square_to_root[i ** 2] = i
        i += 1

print(square_to_root)