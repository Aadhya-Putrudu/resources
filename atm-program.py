class Atm:
    def input(self):
        self.balance=10000
        self.passcode=1234
        self.pin=int(input("Enter pin:"))
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Available Balance")

class Withdraw(Atm):
    def withdraw_amount(self):
        self.amount = int(input("Enter amount:"))
        if (self.pin == self.passcode ):
            if( self.balance>=self.amount):
                self.balance = self.balance - self.amount
                print("Updated balance", self.balance)
            else:
                print("Insufficient Balance.")
        else:
            print("Please enter correct pin.")


class Deposit(Withdraw):
    def deposit_amount(self):
        self.amount = int(input("Enter amount:"))
        if (self.pin == self.passcode):
            self.balance = self.balance + self.amount
            print("Updated balance", self.balance)
        else:
            print("Please enter correct pin.")

class Balance(Deposit):
    def check_balance(self):
        if (self.pin == self.passcode):
            print("Available Balance:", self.balance)
        else:
            print("Please enter correct pin.")


debit=Balance()
debit.input()
choice=int(input("Enter your choice:"))
if(choice==1):
    debit.withdraw_amount()
elif(choice==2):
    debit.deposit_amount()
elif(choice==3):
    debit.check_balance()
else:
    print("Please enter correct value.")
