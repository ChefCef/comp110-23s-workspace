"""EX05 - Utils ig."""

__author__ = "730485079"


def only_evens(dalist: list[int]) -> list[int]:
    """Gives me the even #s."""
    returns: list[int] = []
    indxvlue: int = 0
    while len(dalist) > indxvlue:
        if dalist[indxvlue] % 2 == 0:
            returns.append(dalist[indxvlue])
        indxvlue = indxvlue + 1
    return returns


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Gives me the concat of the #."""
    final_list: list[int] = []
    for number in list1:
        final_list.append(number)
    for number in list2:
        final_list.append(number)
    return final_list


def sub(a_list: list[int], num1: int, num2: int) -> list[int]:
    """Gives me sub of #s."""
    final_list: list[int] = []

    if len(a_list) == 0:
        return final_list
    if num1 < 0:
        num1 = 0
    if num1 == len(a_list):
        return final_list
    if num2 <= 0:
        return final_list
    if num2 >= len(a_list):
        num2 = len(a_list)

    while num1 < num2:
        final_list.append(a_list[num1])
        num1 = num1 + 1
        
    return final_list