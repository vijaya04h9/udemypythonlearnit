# name = input()
# print("Hello, world! Hello, " + name)

# name = input()
# print("Hello, world! Hello, ", name)

# string = input("Enter a string:")
# print(len(string))

# empty_string = ""
# print(len(empty_string))

# def sum_numbers(a, b):
#     return a + b

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = sum_numbers(num1, num2)
# print("The sum is:", result)


# def greet_user(name):
#     return "Hello, " + name + "!"

# name = input("Enter your name: ")
# message = greet_user(name)
# print(message)

def process_string(s):
    return f"The string '{s}' has {len(s)} characters."

user_input = input("Enter a string: ")
result = process_string(user_input)
print(result)

