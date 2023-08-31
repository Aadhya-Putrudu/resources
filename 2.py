# Sum of n natural numbers

print("It is a program to calculate the sum of first n natural numbers. If the input is 5, then output will be 15(1+2+3+4+5).")
num=int(input("Enter a number:"))

Sum=0
for i in range(1,num+1):
    Sum+=i

print(f"The sum of first {num} natural numbers is",Sum)