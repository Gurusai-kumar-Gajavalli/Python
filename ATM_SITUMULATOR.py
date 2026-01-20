class ATM:
    def __init__(self,account_holder,pin,balance=0):
        self.account_holder=account_holder
        self.__pin= pin
        self.balance=balance
        self.transaction_history=[]
        self.attempts=5
    def check_balance(self,pin):
        if self.__pin==pin:
            return self.balance
        else:
            print("Incorrect pin and the attempts left are :",self.attempts-1)
    def deposit(self,amount):
        amount=int(input("Enter the amount to be deposited:"))
        if amount<=0:
            print("Invalid the amount to be deposited")
        self.balance+=amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"deposited amount of {amount}.new balance is {self.balance}")
    def withdraw(self,amount,pin):
        if self.__pin==pin:
            amount=int(input("Enter the amount to be withdraw:"))
            if amount<=0:
                print("Invalid the amount to be withdraw")
            elif amount>self.balance:
                print("Insufficent balance")
            else:
                self.balance-=amount
                self.transaction_history.append(f"Withdrawn: {amount}")
                print(f"withdraw amount of {amount}.new balance is {self.balance}")
    def change_pin(self,old_pin,new_pin):
        old_pin=input("Enter the old pin:")
        if self.__pin==old_pin:
            new_pin=input("Enter the new pin:")
            self.__pin=new_pin
            print("Pin changed successsfully")
        else:
            print("Incorrect old pin")
    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

while True:
    print("\nWelcome to the ATM Simulator")
    name=input("Enter the account holder name:")
    pin=input("Set your 4-digit pin:")
    atm=ATM(name,pin,)
    while True:
        print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Change Pin\n5.Transaction History\n6.Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            pin=input("Enter your pin:")
            print("Your balance is:",atm.check_balance(pin))
        elif choice=='2':
            atm.deposit(0)
        elif choice=='3':
            pin=input("Enter your pin:")
            atm.withdraw(0,pin)
        elif choice=='4':
            old_pin=input("Enter your old pin:")
            new_pin=input("Enter your new pin:")
            atm.change_pin(old_pin,new_pin)
        elif choice=='5':
            atm.transaction_history()
        elif choice=='6':
            print("Thank you for using the ATM Simulator.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        
        