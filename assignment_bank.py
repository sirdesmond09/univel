class Bank():
    
    def __init__(self, name, bal = 0):
        self.name = name
        self.balance = bal

    def cash_deposit(self):
        money = float(input("Enter amount to deposit\n> $"))
        self.balance = money + self.balance
        print(f"Your account has been credited with ${money}\nCurrent balance is ${self.balance}")

    def cash_withdraw(self):

        money = float(input("Enter amount to withdraw\n$" ))
        if money > self.balance:
            print("Insufficient Funds")
            print(f"Your current account balance is ${self.balance}")
            choose = float(input("Enter amount to withdraw or '1' to cancel transaction"))
            if choose == 1:
                exit()
            else:
                self.balance = self.balance - money
                print(f"Your account has been debited with ${money}\nCurrent balance is ${self.balance}")
        else:
            self.balance = self.balance - money
            print(f"Your account has been debited with ${money}\nCurrent balance is ${self.balance}")

    def check_balance(self):
        print(f'Your  current balance is ${self.balance}')

    def transfer(self):
        money = float(input("Enter amount to transfer\n$" ))
        if money > self.balance:
            print("Insufficient Funds")
            print(f"Your current account balance is ${self.balance}")
            choose = float(input("Enter amount to transfer or '1' to cancel transaction"))
            if choose == 1:
                exit()
            else:
                self.balance = self.balance - money
                print(f"Your account has been debited with ${money}\nCurrent balance is ${self.balance}")
        else:
            self.balance = self.balance - money
            print(f"Your account has been debited with ${money}\nCurrent balance is ${self.balance}")



print("Welcome to Our BANK")
print("Create an account below")
name = input("Enter your account name\n> ")
newaccount = AccountHolder(name= name)
newaccount.cash_deposit()
newaccount.cash_withdraw()
newaccount.transfer()
newaccount.check_balance()