"""Example of class and object instantiation."""


class Pizza: 
    """Models the idea of a Pizza."""

    # Attribute Definitions, with defaults for extra cheese
    size: str
    toppings: int
    extra_cheese: bool = False

    def __intit__(self, size: str, toppings: int, extra_cheese: bool):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    # Adding capability
    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
         
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total *= tax

        return total


a_pizza: Pizza = Pizza()
# Supposed to be a_pizza: Pizza = Pizza("large", 3)

print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza()
# Supposed to be another_pizza("small", 0)
print(a_pizza.size)