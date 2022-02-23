"""EX05 - 'list' Utility Functions."""

__author__ = "730464966"


def only_evens(xs: list[int]) -> list[int]:
    """Function that take a list of int and return a list of the integers that are even."""
    i: int = 0
    # While loop used to remove odd integers from list as looping through items in list
    while i < len(xs):
        item: int = xs[i]
        if item % 2 != 0:
            xs.pop(i)
        i += 1
    return xs


def sub(xs: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a subset of a list between start index and end index, exclusive."""
    subset: list[int] = list()
    # If start index is less than 0, start index will be 0
    i: int = start_index
    if start_index < 0:
        i = 0
    if end_index > len(xs):
        end_index = len(xs) - 1
    # If list is empty, start index is higher than lenght of list or end index is less or equal to 0, a empty list is returned
    if len(xs) == 0 or start_index >= len(xs) or end_index <= 0:
        return subset
    # Starting at start index, adding each integer at index i until end index, non inclusive
    while i < end_index:
        subset.append(xs[i])
        i += 1
    return subset


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Generates a list that contains integers from xs followed by integers in ys."""
    i: int = 0
    # Creates a new list
    new_list: list[int] = list()
    # First adding each of xs to new list by use of while loop
    while i < len(xs):
        new_list.append(xs[i])
        i += 1
    i = 0
    # Then adding each of ys to new list by use of while loop
    while i < len(ys):
        new_list.append(ys[i])
        i += 1
    return new_list