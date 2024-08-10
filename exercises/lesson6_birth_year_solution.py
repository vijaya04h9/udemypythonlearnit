from datetime import datetime
#current_year = 2024
birth_year = input("Enter your birth year:\n")
current_year = datetime.now().year

age = current_year - int(birth_year)

print(f"You are approximately {age} years old.")