# The basic syntax of a while loop
# while condition:
# code block

# Example 1: Printing Numbers
count = 1
while count <= 5:
    print(count)
    count +=1

# Example 2: Summing Numbers
total = 0
number = 0
while number >= 0:
    total += number
    number = int(input("Enter a number (negative to quit): "))
print("The sum is:", total)

# Exmaple 3: Guessing Game
import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a secret number (between 1 and 100): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print("Congratulations! You guessed the secret number:", secret_number)


