"""EX03 - Structured Wordle."""

__author__ = "730464966"


def contains_char(searched_word: str, searched_char: str) -> bool:
    """Function that looks to for a specific character in a given word."""
    assert len(searched_char) == 1
    i: int = 0
    char_found: bool = False
    # variable to track whether character found
    while i < len(searched_word):
        if searched_word[i] == searched_char:
            char_found = True
        i += 1
        # if character found at index i then define variable to true, then continue to next index
    if char_found is True:
        return True
        # returning True if character found
    else:
        return False
        # returning False if character not found


def emojified(guess_word: str, secret_word: str) -> str:
    """Returns a string of emoji based on guesswords match with character in secret word."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result_emoji: str = ""
    # varible to store the result for emoji at each index
    while i < len(guess_word):
        if guess_word[i] == secret_word[i]:
            result_emoji += GREEN_BOX
            # if character found at index, green box is added
        else:
            emoji_found_char: bool = True
            if emoji_found_char and contains_char(secret_word, guess_word[i]):
                result_emoji += YELLOW_BOX
                # if character is found in word, yellow box is added
            else:
                result_emoji += WHITE_BOX
                # if character not found in word, green box is added 
        i += 1
    return result_emoji


def input_guess(expected_length: int) -> str:
    """Function to check if user input correct lenght and return guess if correct lenght."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
        # as long as user input wrong length word, user will be asked for new input
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRETWORD: str = "codes"
    number_guessed: int = 1
    # variable to store the amount of guesses used out of 6 possible in the game
    guessed_word: str = ""
    while number_guessed <= 6:
        # this determines that there are six possible guesses, it is also written into the strings below
        print(f"=== Turn {number_guessed}/6 ===")
        guessed_word = input_guess(len(SECRETWORD))
        print(emojified(guessed_word, SECRETWORD))
        if guessed_word == SECRETWORD:
            print(f"You won in {number_guessed}/6 turns!")
            number_guessed = 8
            # escape while loop, if the user guessed correctly 
        else:
            number_guessed += 1
            # continues to next guess if user didn't guess correctly
    if number_guessed == 7:
        print("X/6 - Sorry, try again tomorrow!")
        # when the user used all 6 guesses


if __name__ == "__main__": 
    main()