"""An example of union types."""
# Used to make more generalized constructors, methods and functions, most usefull as parameters type

from typing import Union


def log(info: Union[int, str]) -> None:
    """Log is a function that can be called with __either__ an int or a str argument."""
    if isinstance(info, str):
        print(f"str: {info.lower()}")
    else:
        print(f"int: {info}")


log("Hello, World.")
log(110)