print("1.Sum of even numbers.")
print("2.Sum of odd numbers.")

choice = int(input("Enter your choice:"))

match choice:
    case 1:
        num = int(input("Enter a number:"))
        Sum = 0
        for i in range(1, num + 1):
            if i % 2 == 0:
                Sum += i

        print(f"The sum of even numbers in the first {num} natural numbers is", Sum)

    case 2:
        num = int(input("Enter a number:"))
        Sum = 0
        for i in range(1, num + 1):
            if i % 2 != 0:  # Change this condition to check for odd numbers
                Sum += i

        print(f"The sum of odd numbers in the first {num} natural numbers is", Sum)
