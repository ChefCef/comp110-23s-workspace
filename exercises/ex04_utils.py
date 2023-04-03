"""EX03 - Structured Wordle - P much just wordle."""

__author__ = "730485079"


def all(first: list[int], second: int) -> bool:
    """Seein if da number is in da list 100%."""
    if len(first) == 0:
        return False
    indxvlue: int = 0
    while len(first) > indxvlue:
        if second != first[indxvlue]:
            return False
        else:
            indxvlue = indxvlue + 1
    return True


def max(input: list[int]) -> int:
    """Finden da max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    basenmber: int = input[0]
    indxvlue: int = 1
    while len(input) > indxvlue:
        if basenmber < input[indxvlue]:
            basenmber = input[indxvlue]
        else:
            indxvlue = indxvlue + 1
    return basenmber


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Seein if the lists match."""
    indxvlue: int = 0
    if len(input1) != len(input2):
        return False
    while len(input1) > indxvlue:
        if input1[indxvlue] != input2[indxvlue]:
            return False
        else:
            indxvlue = indxvlue + 1
    return True
