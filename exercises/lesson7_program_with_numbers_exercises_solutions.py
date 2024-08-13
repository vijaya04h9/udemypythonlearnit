# 1. Grocery Budget Calculator
# Hint: Use float() for input and multiply weekly by 4
# Calculate monthly grocery expenses

# weekly_groceries = float(input("Enter your weekly grocery spending: $"))
# weekly_groceries = weekly_groceries * 4
# print(f"Your monthly grocery expenses: ${weekly_groceries}")

# 2. Temprature Converter
# Convert Celsius to Fahrenheit
# Hint: Formula is (C * 9/5) + 32

# celsius = float(input("Enter temprature in Celsius:"))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}C is equal to {fahrenheit}F")

# 3. Tip Calculator
# Calculate tip amount
# Hint: Tip = bill amount * (tip percentage / 100)

# bill_amount = float(input("Enter bill amount: $"))
# tip_percentage = float(input("Enter the tip percentage: "))
# tip_amount = bill_amount * (tip_percentage / 100)
# print(f"The tip amount is: ${tip_amount}")

# 4. Savings Goal Tracker
# Calculate months to reach the savings
# Hint: Divide goal by monthly savings

# savings_goal = float(input("Enter your savings goal: $"))
# monthly_savings = float(input("Enter your monthly savings: $"))
# months_to_goal = savings_goal / monthly_savings 
# print(f"It will take {months_to_goal} months to reach your goal")

# 5.1. Simple Paint Calculator
# TODO: Calculate gallons of paint needed
# Hint: Divide total wall area by paint coverage per gallon

# wall_area = float(input("Enter the total wall area in square feet: "))
# paint_coverage = float(input("Enter the paint coverage per gallon: "))
# paint_needed = wall_area / paint_coverage
# print(f"You need {paint_needed} gallons of paint")

# 5.2. Advanced Paint Calculator
# Calculate gallons of paint needed
# TODO: Same as for 'Simple Paint Calculator'
# TODO: Use different rounding methods (round up, round down, and use round())
# TODO: Create a custom rounding to nearest integer,
# multiply by 2, round to the nearest integer then divide by 2
# ('round()' custom rounding to nearest half of the gallon)
# TODO: Use the ':.2f' format specifier showing 2 decimal places for the float values.
# Hint: Divide total wall area by paint coverage per gallon. Use 'math'
# module. 'math.ceil()' rounds up to the neares integer, 'math.floor' 
# rounds down to the nearest integer. 'round()' rounds to the nearest
# integer (0.5 rounds up to 1).

# import math  # Import the math module for advanced mathematical operations

# # Get input from the user
# wall_area = float(input("Enter the total wall area in square feet: "))
# paint_coverage = float(input("Enter the paint coverage per gallon: "))
# paint_needed = wall_area / paint_coverage

# # Different rounding methods
# # math.ceil() rounds up to the nearest integer
# ceil_round = math.ceil(paint_needed)

# # math.floor() rounds down to the nearest integer
# floor_round = math.floor(paint_needed)

# # round() rounds to the nearest integer (0.5 and above rounds up)
# normal_round = round(paint_coverage)

# # Custom rounding to the nearest half gallon
# # Multiply by 2, round to the nearest integer, then divide by 2
# round_to_half = round(paint_needed * 2) / 2

# # Print the results
# # THe :.2f format specifier shows 2 decimal places for float values
# print(f"Exact amount: {paint_needed:.2f} gallons of paint.")
# print(f"Rounded up (ceiling):{ceil_round} gallon(s).")
# print(f"Rounded down (floor):{floor_round} gallon(s).")
# print(f"Normal round:{normal_round} gallon(s).")
# print(f"Rounded to nearest half gallon:{round_to_half:.1f}gallon(s).")

# 6. Fuel Efficiency Calculator
# Calculate miles per gallon
# Hint: DIvide miles driven by gallons used

# miles_driven = float(input("Enter miles driven: "))
# gallons_used = float(input("Enter gallons of fuel used: "))
# miles_per_gallon = miles_driven / gallons_used
# print(f"Your car's fuel efficiency is {miles_per_gallon} miles per gallon")

# 7. BMI Calculator
# Calculate Body Mass Index
# Hint: BMI = weight (kg) / (height (m) ** 2)

# weight_kg = float(input("Enter your weight in kilograms: "))
# height_m = float(input("Enter your height in meters: "))
# bmi = weight_kg / (height_m ** 2) 
# print(f"Your BMI is:{bmi}")

# 8. Currency Converter
# TODO: Convert USD to EUR
# Hint: Multiply USD amount by exchange rate

# usd_amount = float(input("Enter amount in USD:"))
# exchange_rate = float(input("Enter the current USD to EUR exchange rate: "))
# eur_amount = usd_amount * exchange_rate
# print(f"${usd_amount}USD is equal to €{eur_amount}EUR")

# 9. Mortgage Payment Calculator
# TODO: Calculate monthly mortgage payment
# Hint: Use the formula: P * (r(1+r)^n) / ((1+r)^n -1)
# Where P = principal, r = monthly rate, n = number of payments 

loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate(%): "))
loan_term_years = float(input("Enter the loan term in years: "))
monthly_payment = (loan_amount * (annual_interest_rate / 1200)) / (1 - (1 + annual_interest_rate / 1200) ** ( - loan_term_years * 12))
print(f"Your monthly mortgate payment is: ${monthly_payment}")