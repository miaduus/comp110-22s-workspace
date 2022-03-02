"""Test file for EX06, dictionary."""

__author__ = "730464966"

from dictionary import invert, count, favorite_color


# Test for the invert function
def test_invert_onepair() -> None:
    """Test inverting a single key-value pair."""
    a: dict[str, str] = {"a": "b"}
    assert invert(a) == {"b": "a"}


def test_invert_several() -> None:
    """Test inverting several key-value pairs."""
    a: dict[str, str] = {"a": "b", "y": "x", "u": "i"}
    assert invert(a) == {"b": "a", "x": "y", "i": "u"}


def test_invert_longer_str() -> None:
    """Test inverting str values that are more than one character."""
    a: dict[str, str] = {"January": "February", "March": "April"}
    assert invert(a) == {"February": "January", "April": "March"}


# Test functions for favorite colors
def test_favorite_colors_onepair() -> None:
    """Test returning favorite color if only one key-value pair is given."""
    a: dict[str, str] = {"Maddie": "blue"}
    assert favorite_color(a) == "blue"


def test_favorite_colors_several() -> None:
    """Test returning favorite color if several key-value pair are given, with one favorite color."""
    a: dict[str, str] = {"Maddie": "blue", "Mia": "pink", "Olivia": "pink"}
    assert favorite_color(a) == 'pink'


def test_favorite_colors_twofavorite() -> None:
    """Test returning favorite color if several key-value pair are given, with two favorite colors."""
    a: dict[str, str] = {"Maddie": "blue", "Mia": "pink", "Olivia": "pink", "Liz": "blue"}
    assert favorite_color(a) == 'blue'


# Test functions for count function
def test_count_one_item() -> None:
    """Test of list containing one item."""
    a_list: list[str] = ["a"]
    assert count(a_list) == {"a": 1}


def test_count_several_items() -> None:
    """Test of list containing one item, none being there more than once."""
    a_list: list[str] = ["a", "b"]
    assert count(a_list) == {"a": 1, "b": 1}


def test_count_multiple_items() -> None:
    """Test of list containing one item, with there being there items that have multiples."""
    a_list: list[str] = ["a", "b", "b", "b"]
    assert count(a_list) == {"a": 1, "b": 3}