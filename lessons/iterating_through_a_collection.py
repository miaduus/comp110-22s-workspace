"""Example of looping through all characters in a string."""

__author__ = "730464966"

user_string: str = input("Give me a string!")

# The varible i is common counter varibale name
# in programming. i is short for iteration
i: int = 0 

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done!")
