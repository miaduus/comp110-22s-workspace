"""Test file for EX05, utils."""

__author__ = "730464966"

from utils import only_evens, sub, concat


# Test for the only evens tests
def test_only_evens_empty() -> None:
    """Test if the only evens function returns empty list."""
    assert only_evens(list()) == []


def test_only_evens_postive_numbers() -> None:
    """Test if function returns list of even integers from a list of positive integers."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_negative_positive_numbers() -> None:
    """Test if function returns a list of even integers from a list of positive and negative integers."""
    xs: list[int] = [-3, -2, -1, 0, 1, 2, 3]
    assert only_evens(xs) == [-2, 0, 2]


def test_sub_empty() -> None:
    """Test of function returns empty list if given empty list."""
    assert sub(list(), 1, 1) == []


def test_sub_positive_numbers() -> None: 
    """Test if subset is found from a list of positive integers."""
    xs: list[int] = [0, 1, 2, 3, 4, 5]
    assert sub(xs, 2, 5) == [2, 3, 4]


def test_sub_negative_positive_numbers() -> None:
    """Test if subset is found from list of positive and negative integers."""
    xs: list[int] = [-1, -2, -3, 0, 1, 2, 3]
    assert sub(xs, 2, 5) == [-3, 0, 1]


def test_sub_index_out_of_range() -> None:
    """Test if function returns empty set if index is out of range."""
    xs: list[int] = [0, 1, 2, 3, 4]
    assert sub(xs, 7, 8) == []


def test_sub_negative_index() -> None:
    """Test if function returns list starting at index 0 if start index is less than 0."""
    xs: list[int] = [0, 1, 2, 3]
    assert sub(xs, -1, 2) == [0, 1]


def test_concat_empty() -> None:
    """Test if function returns empty list if two empty lists is input for function."""
    assert concat(list(), list()) == []


def test_concat_one_empty() -> None:
    """Test if function returns one list if other list is empty."""
    xs: list[int] = [1, 2, 3, 4]
    assert concat(xs, list()) == [1, 2, 3, 4]


def test_concat_positive_numbers() -> None:
    """Test if function returns the list of xs followed by ys for two list of positive numbers."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [1, 2, 3, 4]
    assert concat(xs, ys) == [1, 2, 3, 4, 1, 2, 3, 4]


def test_concat_negative_positive_numbers() -> None:
    """Test if function returns the list of xs followed by ys for two list of positive and negative numbers."""
    xs: list[int] = [-3, -1, 1]
    ys: list[int] = [-2, 0, 2]
    assert concat(xs, ys) == [-3, -1, 1, -2, 0, 2]
