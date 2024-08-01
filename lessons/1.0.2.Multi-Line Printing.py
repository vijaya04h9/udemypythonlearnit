# 1. Multiple print() statements:
print("Hello!")
print("Welcome to our multi-line")
print("printing adventure!")

# 2. Using \n for new lines:
print("Line 1\nLine 2\nLine 3")

# 3. Using triple quotes:
print('''This is line 1.
This is line 2.
And this is line 3.''')

# 4. Mixing methods:
print("First line\nSecond line")
print('''Third line
Fourth line''')
print("Fifth line")

# 5. Using escape characters:
print("Let's add a\ttab and a\nnew line!")

# 6. Printing blank lines:
# Method 1: Empty print()
print("First line")
print()  # This prints a blank line
print("Third line")

# Method 2: Using \n
print("First line\n\nThird line")

# Method 3: Triple quotes with line breaks
print("""First line

Third line""")

# 7. Advanced: Formatted multi-line printing with blank lines
name = "Alice"
age = 25
hobby = "coding"

print(f"""Name: {name}

Age: {age}

Hobby: {hobby}""")