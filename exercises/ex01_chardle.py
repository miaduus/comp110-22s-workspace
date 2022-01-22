"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730464966"

guess_word: str = input("Enter a 5-character word: ")
if len(guess_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
guess_single_character: str = input("Enter a single character: ")
if len(guess_single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + guess_single_character + " in " + guess_word)
matching_characters = 0

if guess_word[0] == guess_single_character:
    print(guess_single_character + " found at index 0")
    matching_characters = matching_characters + 1
if guess_word[1] == guess_single_character: 
    print(guess_single_character + " found at index 1")
    matching_characters = matching_characters + 1
if guess_word[2] == guess_single_character:
    print(guess_single_character + " found at index 2")
    matching_characters = matching_characters + 1
if guess_word[3] == guess_single_character:
    print(guess_single_character + " found at index 3")
    matching_characters = matching_characters + 1
if guess_word[4] == guess_single_character:
    print(guess_single_character + " found at index 4")
    matching_characters = matching_characters + 1

if matching_characters == 0:
    print("No instances of " + guess_single_character + " found in " + guess_word)
else:
    if matching_characters == 1:
        print(str(matching_characters) + " instance of " + guess_single_character + " found in " + guess_word)
    else:
        print(str(matching_characters) + " instances of " + guess_single_character + " found in " + guess_word)