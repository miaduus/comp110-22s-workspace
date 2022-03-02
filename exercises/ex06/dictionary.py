"""EX06 - Dictionary Functions."""

__author__ = "730464966"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts keys and values in a dictionary."""
    result: dict[str, str] = {}
    for key in a_dict:
        result[a_dict[key]] = key
    if len(a_dict) == len(result):
        return result
    else:
        raise KeyError


def favorite_colors(a_dict: dict[str, str]) -> str:
    """Function that takes dict of people and their favorite color and returns the most common color."""
    favorite_list: list = []
    b_list: list[str] = []
    # Collecting values of dict in a list
    for key in a_dict:
        b_list.append(a_dict[key])
    # Creating a dict with values and number of times there were in dict by using count function
    c_dict: dict[str, int] = count(b_list)
    d_list: list[int] = []
    # Collecting the numbers of times the colors were in dict a
    for key in c_dict:
        d_list.append(c_dict[key])
    # Creating a list of the favorite color(s), the returning 
    # the color at index 0
    for key in c_dict:
        if c_dict[key] == max(d_list):
            favorite_list.append(key)
    return favorite_list[0]


def count(a_list: list[str]) -> dict[str, int]:
    """Function given a list will return a dict of keys from list and values of times key was found in list."""
    result_dict: dict[str, int] = {}
    i: int = 0
    while i < len(a_list):
        if a_list[i] in result_dict:
            result_dict[a_list[i]] += 1
            i += 1
        else:
            result_dict[a_list[i]] = 1
            i += 1
    return result_dict
