def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"The average is: {average}")

#Example usage with a list containing strings
string_list = [1,2,"three"]
average = calculate_average(string_list)
print(f"The average is: {average}")