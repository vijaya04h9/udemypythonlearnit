# Task: 
# 1. Add one more item to buy
# 2. Calculate the average cost of all items.

# Shopping Calculator
print("Running 'Shopping Calculator App':")
wallet = 50  # You start with 50$

# Buy Some Items
book = 15
snack = 5
drink = 3
hat = 12  # New item added

# Calculate total spent
total_spent = book + snack + drink + hat

# Calculate remaining money
money_left = wallet - total_spent

# Calculate average cost of items
number_of_items = 4  # We now have 4 items
average_cost = total_spent / number_of_items


print("You spent in $", total_spent)
print("You have in $", money_left, "left")
print("The average cost per item is $", average_cost)

