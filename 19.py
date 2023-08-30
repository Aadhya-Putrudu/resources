# Get two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap the numbers without using a third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Print the swapped values
print(f"After swapping, the first number is {num1} and the second number is {num2}")




'''
# Get two numbers as input from the user
num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swap the numbers using XOR bitwise operator
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

# Print the swapped values
print(f"After swapping, the first number is {num1} and the second number is {num2}")

'''




'''
# Get two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap the numbers using tuple unpacking
num1, num2 = num2, num1

# Print the swapped values
print(f"After swapping, the first number is {num1} and the second number is {num2}")

'''