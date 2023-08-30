#count digits in a number

num=int(input("Enter a number:"))
digits = 0 #initialise count to zero
if num<0:
    num= num*-1
while num > 0:
    digits +=1
    num=int(num/10)
print ("The no. of digits is", digits)

'''
# Get the number as input from the user
number = int(input("Enter a number: "))

# Convert the number to a string
number_str = str(number)

# Calculate the number of digits
num_digits = len(number_str)

# Print the result
print(f"The number {number} has {num_digits} digits.")

'''




'''
# Get the number as input from the user
number = int(input("Enter a number: "))

# Convert the number to a string
number_str = str(number)

# Create a list to store the individual digits
digits_list = list(number_str)

# Calculate the number of digits
num_digits = len(digits_list)

# Print the result
print(f"The number {number} has {num_digits} digits.")

'''




'''
def count_digits_recursive(n):
    if n == 0:
        return 0
    return 1 + count_digits_recursive(n // 10)

# Get the number as input from the user
number = int(input("Enter a number: "))

# Calculate the number of digits using recursion
num_digits = count_digits_recursive(number)

# Print the result
print(f"The number has {num_digits} digits.")

'''