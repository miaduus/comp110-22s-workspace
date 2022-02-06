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
        # Progress towards goal; going through each of the characters
    if char_found is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Give back emoji determined by character match."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # Defining constants for emojis 
    a: int = 0
    emoji_guess: str = ""
    while a < len(guess):
        if guess[a] == secret[a]:
            emoji_guess = emoji_guess + GREEN_BOX
            # If character at same index
        else:
            character_match: bool = False
            if character_match == contains_char(secret, guess[a]):
                emoji_guess = emoji_guess + YELLOW_BOX
                # Using function to search if char is in word, if true add yellow box
            else:
                emoji_guess = emoji_guess + WHITE_BOX
                # If False, character not in word, add white box
    a = a + 1
    return emoji_guess