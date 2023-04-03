"""A cool lil function called zip"""

__author__ = "730485079"

def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    returns: dict[str, int] = {}
    if len(keys) == 0 or len(values) == 0:
        return returns
    if len(keys) != len(values):
        return returns
    for index in range(0, len(keys)):
      returns[keys[index]] = values[index]
    return returns