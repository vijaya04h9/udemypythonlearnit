print("Common Mistakes with Python Print Statements")
print("-" * 40)

# 1. Forgetting parentheses
print("\n1. Forgetting parentheses:")
# print "Oops!"  # Uncomment to see the SyntaxError
print("Correct: print('Hello')")

# 2. Mismatched quotes
print("\n2. Mismatched quotes:")
# print("This is wrong')  # Uncomment to see the SyntaxError
# print('She said "Hello" and left.)  # Uncomment to see the SyntaxError
print("Correct: print('She said \"Hello\" and left.')")

# 3. Incorrect indentation
print("\n3. Incorrect indentation:")
if True:
    print("Correct indentation")
    # print("Too much indentation")  # Uncomment to see the IndentationError

# 4. Case sensitivity
print("\n4. Case sensitivity:")
# Print("Python is case-sensitive!")  # Uncomment to see the NameError
# PRINT("This won't work either")    # Uncomment to see the NameError
print("Correct: print('Python is case-sensitive!')")

# 5. Forgetting to close parentheses
print("\n5. Forgetting to close parentheses:")
# print("Oops, I forgot to close the parenthesis"  # Uncomment to see the SyntaxError
print("Correct: print('Remember to close parentheses')")

# 6. Using commas incorrectly
print("\n6. Using commas incorrectly:")
print("Hello", "world")  # This works, but adds a space between words
print("Hello" + "world")  # This works too, but doesn't add a space
# print("Hello" + , + "world")  # Uncomment to see the SyntaxError
print("Correct: print('Hello' + ' ' + 'world')  # If you want to concatenate with a space")

# 7. Mixing up string formatting
print("\n7. Mixing up string formatting:")
name = "Alice"
print("Old style: Hello %s" % name)
print("Newer style: Hello {}".format(name))
print(f"f-string (Python 3.6+): Hello {name}")
print("Literal (incorrect): Hello {name}")

# 8. Forgetting to convert numbers to strings
print("\n8. Forgetting to convert numbers to strings:")
age = 25
# print("I am " + age + " years old")  # Uncomment to see the TypeError
print("Correct: print('I am ' + str(age) + ' years old')")
print("Alternative: print('I am', age, 'years old')")
print(f"Using f-string: print(f'I am {age} years old')")

# 9. Using backslashes incorrectly
print("\n9. Using backslashes incorrectly:")
# print("This will cause an error: \")  # Uncomment to see the SyntaxError
print("Correct: print('This works: \\')")

# 10. Printing variables that don't exist
print("\n10. Printing variables that don't exist:")
# print(undefined_variable)  # Uncomment to see the NameError
print("Correct: Make sure the variable is defined before printing")

print("\nRemember: Learning from mistakes is a crucial part of becoming a better programmer!")

# Bonus: Practice section
print("\nPractice Section:")
print("Try uncommenting these lines one by one and fix the errors:")
# print('Let's practice finding errors')
# print "No parentheses here"
# Print("Oops, capitalized 'Print'")
# print("Forgot to close the parenthesis"
# print("Using" + , + "commas incorrectly")