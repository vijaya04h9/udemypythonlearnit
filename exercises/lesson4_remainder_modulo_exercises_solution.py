# 1. Movie Theater Seating

# You're managing a small movie theater with 50 seats, 
# and a group of 7 peaple wants to sit togather in the same row. 
# How many complete rows can you fill, 
# and how many seats will be left over in the partially filled row?

# Set the variable
total_seats = 50
group_size = 7

# Calculate the number of full rows
full_rows = total_seats // group_size

# Calculate leftover seats
left_over_seats = total_seats % group_size

# Print out the results
print(f"Number of full rows: {full_rows}")
print(f"Leftover seats in the last row: {left_over_seats}")


# 2. Decode the Secret Message

# You've just intercepted an encoded message . 
# The message is a string of numbers, but you know their 
# encryption method: each letter of the alphabet is represented by its 
# position (A=1, B=2, C=3...Z=26), and these numbers are then 
# concatenated into one long string. You need to decode the last 
# letter of this secret message. 

# 1. Extract the last digit of the encoded message.
# 2. Use this to determine the correstponding letter. 
# 3. Report back with the decoded letter.

encoded_message = 1233248916372176409

# Revealing the last letter
last_digit = encoded_message % 26

# Converting the digit to a letter (A=0, B=1 etc)
decoded_letter = chr(last_digit + 65)

print(f"The last letter of the secret message is: {decoded_letter}")


