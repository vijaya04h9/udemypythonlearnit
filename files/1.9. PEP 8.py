# PEP 8: The Python Style Guide

# 1. Introduction to PEP 8

# 2. Code Layout
# Indentation

if True:
    print("This is correctly indented")
    if True:
        print("This is the second level of indentation")

# Maximum Line Length
# PEP 8 recommends keeping lines at a maximum of 79 characters.

long_string = (
    "This is a very long string that I've broken up "
    "over multiple lines for better readability. "
    "Notice how the parentheses allow us to do this."
)

print(long_string)


# 3. Naming Conventions
# Function names (lowercase with underscores)

def function_name():
    pass


# Variable names (lowercase with underscores)
my_variable = 42


# Class names (CamelCase)
class MyClass:
    pass


# Method names (lowercase with underscores)
class MyClass:
    def my_method(self):
        pass
