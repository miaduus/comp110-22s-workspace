"""EX03 - Structured Wordle."""

__author__ = "730464966"


def contains_char(search_word: str, search_char: str) -> bool:
    """Function to search for character in a given word."""
    assert len(search_char) == 1
    i: int = 0
    char_found: bool = False
    while i < len(search_word):
        if search_char == search_word[i]:
            char_found = True
            # Search for character if found true
        i = i + 1
    if char_found is True:
        return True
    else:
        return False
