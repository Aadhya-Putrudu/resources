pin=4589
cash=10000

passcode=int(input("Enter atm password:"))

if pin==passcode:
	print("Welcome")
	print("1.Cash Withdraw")
	print("2.Cash Deposit")
	print("3.Exit")
	choice=int(input("Select one option:"))
	if choice==1:
		withdraw_amount=int(input("Enter amount to withdraw:"))
		if withdraw_amount>cash:
			print("Insufficient amount in your account.")
		else:
			print("Your transaction successfull. \nTake your Cah. \nThank you")
			cash=cash-withdraw_amount
else:
	print("Invalid Password")