# Using PEP8 exmaples

def calculate_area(length, width)  # Good
def CalculateArea(length, width)  # Not recommended

my_variable = 42  # Good
myVariable = 42  # Not recommended

class CarEngine:  # Good
class car_engine:  # Not recommended
  
MAX_SPEED = 120  # Good
max_speed = 120  # Not recommened for constants

# Using PEP8 best practices example
# Code to check (incorrect version)
def CALCULATE_sum(a,b):
    return a+b

result=CALCULATE_sum(10,20)
print("The sum is: "+str(result))

# Corrected code (correct version)
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print(f"The sum is: {result}")