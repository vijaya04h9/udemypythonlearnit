# Strings in Python
greeting = "Hello, world!"
name = "Alice"

# Length of a string
# Using len() function to get the length of a string
print(len(greeting))  # Output: 13

# Indexing
print(greeting[0])  # Output: H
print(greeting[2])  # Output: l
print(name[-1])  # Output: e

# Slicing
# The syntax is string[start:end:step]
print(greeting[0:5])  # Output: Hello
print(name[1:3])  # Output: li
print(greeting[::-1])  # Output: !dlrow ,olleH
print(greeting[::-2])  # Output: !lo olH

# Concatenation with '+'
full_name = name + 'Wonderland'
full_name_space = name + ' ' + 'Wonderland'
print(full_name)  # Output: AliceWonderland
print(full_name_space)  # Output: Alice Wonderland

# Repetition with '*'
chant = name*3
print(chant)  # Output: 'AliceAliceAlice'

# Using String Methods
print(greeting.upper())  # Output: HELLO, WORLD!
print(name.lower())  # Output: alice
print(name.replace('l','i'))  # Output: Axice
