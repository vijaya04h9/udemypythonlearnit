# This is our secret number for today;s order
receipt_order = 2468

# Read the customer's input
slices = int(input("How many pizza slices did you order? "))
price_per_slice = int(input("What was the price per slice? "))

# Calculate the total
order_total = slices * price_per_slice

# Check if the order total matches our receipt number
print(order_total == receipt_order)