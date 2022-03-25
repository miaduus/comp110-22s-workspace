"""Examples of default parameters."""
# Common in constructor definitions


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Example of a default parameter where y and z are 0 by default."""
    return x + y + z


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
