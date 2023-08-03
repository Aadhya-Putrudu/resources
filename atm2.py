pin=5454
cash=5000
password=int(input("enter ur secure password"))
if password==pin:
	print("welcome")
	print("1.withdraw")
	print("2.deposit")
	print("3.exit")
	option=int(input("select your option"))
	if option==1:
		print("withdraw")
		with_draw=int(input("wnter withdraw amount"))
		if cash>with_draw:
			print("transaction successfull")
			cash=cash-with_draw
			print("avilablbe balnse",cash)
		else:
			print("insfuciant balnce in ypur acount")
	elif option==2:
		print("depoist")
		deposit=int(input("enter your amount"))
		cash=cash+deposit
		print("avialble balnse",cash)
	elif option==3:
		print("exit")
		print("tq for visting")
else:
	print("wrong password")
