#Print all even numbers between 1 to N

num=int(input("Enter a natural number:"))
print(f"List of even numbers between 0 and {num}:")
for i in range(0,num+1):
    if(i%2==0):
        print(i)