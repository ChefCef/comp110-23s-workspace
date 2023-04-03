"""EX02 - One Shot Wordle - Another step toward Wordle."""

__author__ = "730485079"

question: str = input("what is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = ("python")

indxvlue: int = 0

output: str = ("")

while len(question) != len(secret):
    question = input(f"That was not {len(secret)} letters! Try Again: ")

while len(secret) > indxvlue:
    if question[indxvlue] == secret[indxvlue]:
        output += GREEN_BOX
    if question[indxvlue] != secret[indxvlue]:
        ifinword: bool = False
        indexvalue2: int = 0
        while indexvalue2 < len(secret) and ifinword == False:
            if question[indxvlue] == secret[indexvalue2]:
                ifinword = True
            else:
                indexvalue2 = indexvalue2 + 1
        if ifinword == True:
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
    indxvlue = indxvlue + 1

print(output)

if question != secret:
    print("Not quite, play again soon")
if question == secret:
    print("Woo! You got it!")