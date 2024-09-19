# The print() function
print("Hello, World!")
print()
print("Bye,", "then!" )

# Using len()
number = "123"
print(len(number))

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# Type conversion
number = "123"
interger = int(number)
float_number = float(number)

# Mathematical operations
integer = 3
float_number = 5.4
print(sum((interger, float_number)))

my_sum = sum((interger, float_number))
print(round(my_sum))

print(min(interger, float_number))
print(max(interger, float_number))

# Combining Functions
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
rounded_average = round(average)
print(f"The rounded average is: {rounded_average}")

# Using type() 
mixed_list = [1, "two", 3.0, [4, 5]]
for item in mixed_list:
    print(f"The type of {item} is {type(item)}")

# String Manipulation
message = "hello, world!"
print(message.upper())

words = message.split(", ")
print(words)

print(", ".join(word.capitalize() for word in words))

fruits = ['apple', "banana", "cherry"]
print(", ".join(fruits))
print(" - ".join(fruits))

word = "Python"
print("".join(reversed(word)))


