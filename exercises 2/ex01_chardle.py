"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730485079"

Word: str = input("Enter a 5-character word: ")

counter = len(Word)
if counter != 5:
    print("Error: Word must contain 5 characters")
    exit()

Character: str = input("Enter a single character: ")

counter1 = len(Character)
if counter1 != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + Character + " in " + Word)

if Character == Word[0]:
    print(Character + " found at index 0")
    if Character == Word[0]:
        Q: int = 1
else:
        Q: int = 0
if Character == Word[1]:
    print(Character + " found at index 1")
    if Character == Word[1]:
        W: int = 1
else:
        W: int = 0
if Character == Word[2]:
    print(Character + " found at index 2")
    if Character == Word[2]:
        E: int = 1
else:
        E: int = 0
if Character == Word[3]:
    print(Character + " found at index 3")
    if Character == Word[3]:
        R: int = 1
else:
        R: int = 0
if Character == Word[4]:
    print(Character + " found at index 4")
    if Character == Word[4]:
        T: int = 1
else:
        T: int = 0

numbers = [Q,W,E,R,T]

sum = sum(numbers)

sumstr = str(sum)


if sum == 1:
        print(sumstr + " instance of " + Character + " found in " + Word)
if sum == 0:
        print("No instances of " + Character + " found in " + Word)
if sum > 1:
        print(sumstr + " instances of " + Character + " found in " + Word)
