# 2138 Yash Parmar
'''Question5 
Write a program to deposit or withdraw money in a bank account.
'''
class Bank:
    # constructor
    def __init__(self):
        self.balance=0
    
    # deposit Method
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Amount Deposited:", amount)
    
    # withdraw Method
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance")
       
    # display Amount 
    def Amount(self):
        print("Available Balance =", self.balance)
 
# creating object of Bank class       
user1 = Bank()
user1.deposit()
user1.withdraw()
user1.Amount()