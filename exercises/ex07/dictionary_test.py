"""EX07 - Util test ig."""

__author__ = "730485079"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert1() -> None:
    """Tests normal use 1."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert2() -> None:
    """Tests normal use 2."""
    assert invert({'turtle': 'pinapple'}) == {"pinapple": "turtle"}


def test_invert3() -> None:
    """Test to see if its empty."""
    assert invert({}) == {}


def test_favorite_color1() -> None:
    """Tests normal use 1."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == {"blue"}


def test_favorite_color2() -> None:
    """Tests normal use 2."""
    assert favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "blue"}) == {"yellow"}


def test_favorite_color3() -> None:
    """Tests if it can handle a tie between colors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Gary": "yellow"}) == {"yellow"}


def test_count1() -> None:
    """Tests normal use 2."""
    assert count(["Gary", "Gary", "Marc"]) == {"Gary": 2, "Marc": 1}


def test_count2() -> None:
    """Tests normal use 2."""
    assert count(["Gary", "Marc", "Marc"]) == {"Gary": 1, "Marc": 2}


def test_count3() -> None:
    """Tests if it can handle a tie."""
    assert count(["Gary", "Gary", "Marc", "Marc"]) == {"Gary": 2, "Marc": 2}
