# Word Game Script

# Get a word from the user
word = input("Enter a word: ")

# Find the length of the word
word_length = len(word)
print(f"The word '{word}' has {word_length} characters.")

# Reverse the word
reversed_word = word[::-1]
print(f"The reversed word is: {reversed_word}")

# Create a new word by repeating the first character
first_char = word[0]
new_word = first_char * word_length
print(f"A new word created by repeating the first character: {new_word}")

# Concatenate the original word with a suffix
suffix = "ish"
word_with_suffix = word + suffix
print(f"The word with the suffix '{suffix}': {word_with_suffix}")

# Convert the word to uppercase
uppercase_word = word.upper()
print(f"The word in uppercase: {uppercase_word}")

# Replace a character in the word
replacement_char = "x"
replaced_word = word.replace("l", replacement_char)
print(f"The word with 'l' replaced by '{replacement_char}': {replaced_word}")