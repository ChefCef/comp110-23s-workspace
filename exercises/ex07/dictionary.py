"""EX07 - Dictionaries."""

__author__ = "730485079"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invertin the input."""
    answer: dict[str, str] = {}
    for values in input:
        davalue = input[values]
        if davalue in answer:
            raise KeyError("Keys must be unique fool")
        answer[davalue] = values
    return answer


def favorite_color(input: dict[str, str]) -> str:
    """Seein what yo fav color is."""
    count_dict: dict[str, int] = {}
    colors_list: list[str] = []
    for students in input:
        colors_list.append(input[students])
    count_dict = count(colors_list)
    max_color: str = colors_list[0]

    for colors in count_dict:
        if count_dict[max_color] < count_dict[colors]:
            max_color = colors
    return max_color


def count(input: list[str]) -> dict[str, int]:
    """Countin' yo list and seein whats up with it."""
    returns: dict[str, int] = {}
    for items in input:
        if items in returns:
            returns[items] += 1
        else:
            returns[items] = 1
    return returns