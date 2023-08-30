# Get charcte rinput from user

ch=input("Enter a character:")

if len(ch)==1:
    # print('The ASCII value of', ch, 'is:', ord (ch))
    print("The entered character is",ch)
else:
    print("Please enter single character only.")