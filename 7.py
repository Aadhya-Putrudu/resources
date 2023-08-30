vowel=['a','e','i','o','u','A','E','I','O','U']

ch=input("Enter a character:")

if len(ch)==1:
    if(ch in vowel):
        print("You entered a vowel.")
    else:
        print("You entered a consonant.")
else:
    print("Please enter single character only.")
