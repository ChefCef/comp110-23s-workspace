""""Input a string and an index, returns the letter at index"""


def mimic_letter(my_word: str, indx: int ) -> str:
    """"Returns same string back to you"""
    if indx >= len(my_word):
        return("Index too high")
    #If we made it here, that means that the letter indx is valid
    return my_word[indx] 