def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"The average is: {average}")

#Example usage with a list containing strings
string_list = [1,2,"three"]
average = calculate_average(string_list)
print(f"The average is: {average}")

# Example usage with a list of numbers
number_list = [1, 2, 3, 4, 5]
average = calculate_average(number_list)
print(f"The average is: {average}") 