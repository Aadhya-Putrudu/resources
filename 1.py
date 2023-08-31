# Program to print first n natural numbers

print("It is a program to first n natural numbers.If you give 5 as input, it prints first 5 natural numbers from 1 to 5.")
num=int(input("Enter a number:"))
print(f"The first {num} natural numbers are:")
for i in range(num):
    print(i+1)