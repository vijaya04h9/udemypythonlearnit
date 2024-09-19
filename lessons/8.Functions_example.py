def process_numbers(numbers):
    total = sum(numbers)
    avarage = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return f"Total: {total}, Average: {round(avarage, 2)}, Min: {minimum}, Max: {maximum}"

result = process_numbers([1, 2, 3, 4 ,5])
print(result)

float_result = process_numbers([1.5, 2.7, 3.2, 4.9, 5.1])
print(float_result)