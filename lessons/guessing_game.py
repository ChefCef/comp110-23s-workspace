""""Asks user for a number, goes until they get it right"""

SECRET: int = 4

guess: int = int(input("Guess a number! "))

playing: bool = True

number_of_guesses: int = 0

while playing or number_of_guesses < 3:
    if guess == SECRET:
        print("Yay! You got it right.")
        playing = False
    else:
        print("Wrong number. :(")
        if guess % 2 == 1: #guess is odd
            print("Sucka, the answer is even not odd")
        if guess > SECRET:
            print("You guess is too high, its lower than that!")
        else: #guess is lower than da secret
            print("Yo guess to low")
        guess = int(input("Make another guess! "))
    number_of_guesses = number_of_guesses + 1
    print("Number of guesses " + str(number_of_guesses))