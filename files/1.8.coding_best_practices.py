def f(x, y):
    z = x + y
    return z


def add_numbers(number_one, number_two):
    """
    Add two numbers and return the result.
    Args:
    number_one (int): The first number to add
    number_two (int): The second number to add

    Returns:
    int: The sum of two numbers

    """
    return number_one + number_two


# Using meaningful names
# Less clear version
def calc(a, b):
    return a * b


# Clearer version
def calculate_rectangle_area(length, width):
    return length * width

area = calculate_rectangle_area(5, 3)
print(f"The area of rectagle is: {area}")




# Usage example
result = add_numbers(5, 7)
print(f"The sum of 5 and 7 is: {result}")
