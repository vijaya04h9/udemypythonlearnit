# Assignment Operators
# Simple assignment
x = 10
print("x =", x)

# Add and assign
x += 5
print("After x += 5, x =", x)

# Subtract and assign
x -= 3
print("After x -=3, x =", x)

# Multiply and assign
x *= 2
print("After x *= 2, x =", x)

# Divide and assign
x /= 4
print("After x /= 4, x =", x)

# Comparison Operators
# Equal to
print("5 == 5:", 5 == 5)
print("5 == 6:", 5 == 6)

# Not equal to
print("5 != 6:", 5 != 6)

# Greater than
print("7 > 3:", 7 > 3)

# Less than
print("2 < 8:", 2 < 8)

# Greater than or equal to
print("5 >= 5:", 5 >= 5 )

# Less than or equal to
print("3 <= 2:", 3 <= 2)

# Logical Operators
# and operator
print("True and True:", True and True)
print("True and False:", True and False)

# or operator
print("True or False:", True or False)
print("False or False:", False or False)

# not operator
print("not True:", not True)
print("not False:", not False)

# Combining logical operators
x = 5
y = 10
z = 15
result = (x < y) and (y < z)
print("(x < y) and (y < z):", result)

result = (x > y) or (y < z)
print("(x > y) or (y < z):", result)