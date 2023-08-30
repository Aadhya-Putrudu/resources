#ASCII value of a character

ch=input("Enter a character:")

if len(ch)==1:
    print('The ASCII value of', ch, 'is:', ord (ch))
else:
    print ("Please enter only one character")
    # print("Please enter single character only.")