"""EX05 - Util test ig."""

__author__ = "730485079"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens1() -> None:
    """Tests normal use 1."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens2() -> None:
    """Tests normal use 2."""
    assert only_evens([4, 4, 5]) == [4, 4]


def test_only_evens3() -> None:
    """Tests if it can handle negatives."""
    assert only_evens([-4, 4, 5]) == [-4, 4]


def test_concat1() -> None:
    """Tests normal use 1."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]


def test_concat2() -> None:
    """Tests normal use 2."""
    assert concat([3, 3, 3], [3, 3, 3]) == [3, 3, 3, 3, 3, 3]


def test_concat3() -> None:
    """Tests if it can handle negatives."""
    assert concat([-1, -2, -3], [1, 2, 3]) == [-1, -2, -3, 1, 2, 3]


def test_sub1() -> None:
    """Tests normal use 2."""
    assert sub([10, 20, 30, 40, 50], 1, 3) == [20, 30]


def test_sub2() -> None:
    """Tests normal use 2."""
    assert sub([10, 20, 30, 40, 50], 1, 4) == [20, 30, 40]


def test_sub3() -> None:
    """Tests if it can handle negatives."""
    assert sub([10, 20, 30, 40, 50], -1, 3) == [10, 20, 30]
