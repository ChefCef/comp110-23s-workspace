"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730485079"

word: str = input("Enter a 5-character word: ")

counter = len(word)
if counter != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

counter1 = len(character)
if counter1 != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + character + " in " + word)


adding: int = 0


if character == word[0]:
    print(character + " found at index 0")
    adding = adding + 1

if character == word[1]:
    print(character + " found at index 1")
    adding = adding + 1

if character == word[2]:
    print(character + " found at index 2")
    adding = adding + 1

if character == word[3]:
    print(character + " found at index 3")
    adding = adding + 1

if character == word[4]:
    print(character + " found at index 4")
    adding = adding + 1     


sumstr = str(adding)


if adding == 0:
    print("No instances of " + character + " found in " + word)
if adding == 1:
    print(sumstr + " instance of " + character + " found in " + word)
if adding > 1:
    print(sumstr + " instances of " + character + " found in " + word)