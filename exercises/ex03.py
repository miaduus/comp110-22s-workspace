"""EX03 - Structured Wordle."""

__author__ = "730464966"


def contains_char(searched_word: str, searched_char: str) -> bool:
    """Function that looks to for a specific character in a given word."""
    assert len(searched_char) == 1
    i: int = 0
    char_found: bool = False
    while i < len(searched_word):
        if searched_word[i] == searched_char:
            char_found = True
        i += 1
    if char_found is True:
        return True
    else:
        return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Returns a string of emoji based on guesswords match with character in secret word."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    j: int = 0
    result_emoji: str = ""
    while j < len(guess_word):
        if guess_word[j] == secret_word[j]:
            result_emoji += GREEN_BOX
        else:
            emoji_found_char: bool = True
            if emoji_found_char and contains_char(secret_word, guess_word[j]):
                result_emoji += YELLOW_BOX
            else:
                result_emoji += WHITE_BOX
        j += 1
    return result_emoji