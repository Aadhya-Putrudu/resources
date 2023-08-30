# Get two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print the swapped values
print(f"After swapping, the first number is {num1} and the second number is {num2}")
