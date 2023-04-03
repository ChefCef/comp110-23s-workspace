"""EX03 - Structured Wordle - P much just wordle"""

__author__ = "730485079"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, char: str) -> bool:
    """Comparing the input guess to the secret"""
    assert len(char) == 1
    indxvlue: int = 0
    while len(word) > indxvlue:
        if char == word[indxvlue]:
            return True
        else: 
            indxvlue = indxvlue + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Adding them emojies"""
    assert len(guess) == len(secret)
    output: str = ("")
    indxvlue: int = 0
    while len(secret) > indxvlue:
        #makes sure you go through whole word to emojify it
        if guess[indxvlue] == secret[indxvlue]:
            output += GREEN_BOX
        if guess[indxvlue] != secret[indxvlue]:
            if contains_char(secret, guess[indxvlue]):
                output += YELLOW_BOX
            else:
                output += WHITE_BOX
        indxvlue = indxvlue + 1
    return output

def input_guess(inputlength: int) -> str:
    """Telling you if you got the letters or not"""
    question: str = input(f"Enter a {(inputlength)} character word: ")
    while len(question) != inputlength:
        question = input(f"That wasn't {(inputlength)} chars! Try Again: ")
    return question

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turnsplayed: int = 1
    correctornot: bool = False
    secret: str = ("codes")
    while turnsplayed <= 6 and correctornot == False:
        #keeps track of the turns and decides how correct guess is
        print(f"=== Turn {(turnsplayed)}/6 ===")
        guess: str = input_guess(len(secret))
        emoji: str = emojified(guess, secret)
        print(emoji)
        if guess == secret:
            print(f"You won in {(turnsplayed)}/6 turns!")
            correctornot = True
        turnsplayed = turnsplayed + 1
    if correctornot == False:
        print("X/6 - Sorry, try again tomorrow! ")

if __name__ == "__main__":
    main()