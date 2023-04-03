def cut(input: dict[str, int]) -> list[int]:
    new_list: list[int] = []
    for animals in input:
        if input[animals] % 2 == 0 and input[animals] < 18:
            new_list.append(input[animals])
    return new_list




