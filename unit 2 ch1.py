#Python program to create Bankaccount class
#with both a deposit() and a withdraw()function
class Bank_Account:
    def __init__(self):
       self.balance=0
       print("Hello!!Welcome to the Deposit&Withdrawal Machine")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited:"))
        self.balance +=amount
        print("\n Amount of Deposited:",amount)
    def withdraw(self):
       amount=float(input("Enter the amount to be Withdraw:"))
       if self.balance>=amount:
               self.balance-=amount
               print("\n You Withdraw:",amount)
       else:
           print("\n Insufficient Balance")
    def display(self):
        print("\n Net Available Balance=",self.balance)
#Driver Code
#creating an object of class 
s=Bank_Account()
#Calling functions with that class object
s.deposit()
s.withdraw()
s.display()


