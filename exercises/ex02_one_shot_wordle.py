"""EX02 - One Shot Wordle and Loops."""

__author__ = "730464966"

secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess?")

# checking lenght if lenght of word is correct
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# defining constants for emoji
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# defining loop index variable and emoji result
i: int = 0
emoji_result: str = ""

# checking each letter in guess to see if match secret word
while i < len(secret_word):
    if secret_word[i] == guess_word[i]:
        emoji_result += GREEN_BOX
        # in case letter match at index position, green box is added
    else:
        letter_match: bool = True
        alternate: int = 0
        # checking if letter is in word
        while letter_match and (alternate < len(secret_word)):
            if secret_word[alternate] == guess_word[i]:
                emoji_result += YELLOW_BOX
                letter_match = False
                # if letter is in word, yellow box is added
            else:
                alternate += 1
                # progress in while loop to check next index number
                if alternate == len(secret_word):
                    emoji_result += WHITE_BOX
                    # if letter is NOT in word, white box is added
    i = i + 1

print(emoji_result)

# print whether the word is guessed correctly or not
if secret_word == guess_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")