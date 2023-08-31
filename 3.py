#Print all odd numbers between 1 to N

num=int(input("Enter a natural number:"))
print(f"List of odd numbers between 1 and {num}:")
for i in range(1,num+1):
    if(i%2==1):
        print(i)