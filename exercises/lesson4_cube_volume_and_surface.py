# Calculating the Volume of a Cube

# To write a program that:
# 1. Stores the length of cube's side (let's say that it's 4 units)
# 2. Calculates the volume using our formula (volume = side length * side length * side length)
# 3. Prints the results to the screen

# 1. Declare the side length
# Use user's input to enter any number they want
side_length = float(input("Enter the side length of a cube:"))
# Uncomment if you want to use predefined side length
#side_length = 4

# 2. Calculate the volume
volume = side_length ** 3

# 3. Print the result
print("The volume of the cube is:", volume)

# Bonus tasks:
# Modify the program to calculate the surface area of the cube (hint: it's 6 ** side_length ** 2)
# Create a program that calculates both volume and surface area, and prints both results. 