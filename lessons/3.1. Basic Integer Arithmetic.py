# Your First Calculations
print(6 + 3)  # Addition
print(6 - 3)  # Subtraction
print(6 * 3)  # Multiplication
print(6 / 3)  # Division
# Using Variables
apples = 6
oranges = 3

total_fruits = apples + oranges
print("Total fruits: ", total_fruits)

fruits_eaten = 2
fruits_left = total_fruits - fruits_eaten
print("Fruits left: ", fruits_left)
print("\n")

# Integer VS Float
print(type(4 + 2))
print(type(4 - 2))
print(type(4 * 2))


# The Devision Surprise
# The / operator always gives a float.
print(type(4 / 2))
print(type(4 / 3))

# Exercise exmaple with devision
print(12 / 3)  # a)4 b)-4 c)4.0 d)-4.0

# Integer Division
# The // operator divides and rounds down (it's called 'floor devision') to the nearest integer. 
print(12 // 3)
print(type(12 // 3))

# Watch out for negative numbers!
print(10 // 3)  # The output is: 3
print(-10 // 3)  # The output is: -4 (not -3)


