#greatest among 3

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

large=num3
if num1>large:
    large=num1
if num2>large:
    large=num2

print(f"{large} is the largest number.")