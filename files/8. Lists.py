# Lists in Python
# Creating Lists
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed = ['hello', 9, True, [1, 2]]

# Accessing List Elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: cherry

# List Slicing list. The syntax is [start:stop:step]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])  # Output: [3, 4, 5, 6]
print(numbers[:4])  # Output: [1, 2, 3, 4] (from start)
print(numbers[4:])  # Output: [5, 6, 7, 8, 9] (to the end)
print(numbers[::2])  # Output: [1, 3, 5, 7, 9] (every other element)

# List Operations
vegetables = ['carrot', 'potato']
combined = fruits + vegetables  # Concatenation
print(combined)  # Output: ['apple', 'banana', 'cherry', 'carrot', 'potato']

repeated = 2 * fruits  # Repetition
print(repeated)   # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

print('banana' in fruits)  # Membership testing, Output: True
print('orange' in fruits)  # Membership testing, Output: False

# List Methods
print(fruits)
fruits.append('orange')  # Appends an element to the end
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1,'grape') # Inserts an element at a specific index
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

fruits.remove('banana')  # Removes the first occurrence of an element
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']

fruits.pop(1)  # Removes and returns the element at a specific index
print(fruits)  # Output: ['apple', 'cherry', 'orange']

fruits.sort()  # Sorts the list in place
print(fruits)  # Output: ['apple', 'cherry', 'orange']




