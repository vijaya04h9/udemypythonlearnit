# Trip Budget Calculater

# Set up your variables here
total_budget = 1500  # Total budget for the trip
gas_cost = 600  # Expected cost for gas
food_cost = 300  # Expected cost for food
accommodation_cost = 200  # Expected cost for accommodation
souvenir_cost = 25  # Cost of each souverir

expenses = gas_cost + food_cost + accommodation_cost
remaining_money = total_budget - expenses

# Calculate the remaining money after expenses
print ("Money left for souvenirs:", remaining_money)

# Calculate the number of souvenirs you can buy 
# Hint: Use integer division (//) for this step
num_souvenirs = remaining_money // souvenir_cost

# Print the result
# Hint: Use an f-string to format your output
print(f"You can buy {num_souvenirs} souvenirs on your trip!")

# Bonus: Calculate and print how much money is left after buying souvenirs
# Hint: Use the modulo operator (%) to get the remainder.
money_left_after_souvenirs = remaining_money % souvenir_cost

print(f"You can buy {num_souvenirs} souvenirs.")
print(f"You will have ${money_left_after_souvenirs} left after buying souverirs.")