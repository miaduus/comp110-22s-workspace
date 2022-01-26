"""Example of boolean operators: or, and, not."""

is_rainy: bool = True
is_cold: bool = False

print(not is_rainy)
# expect False
print(is_rainy and is_cold)
# expect False
print(is_rainy or is_cold)
# expect True

if is_rainy or is_cold:
    print("Bring a jacket!")
else: 
    print("Don't bring a jacket")
