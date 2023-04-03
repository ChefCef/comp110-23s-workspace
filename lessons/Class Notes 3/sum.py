

def sum(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    for elem in range(0, len(xs)):
        elem = xs[idx]
        sum_total += elem
        idx += 1
    return sum_total

