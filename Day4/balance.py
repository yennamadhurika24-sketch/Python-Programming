class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if(self.__balance>=amount):
            self.__balance-=amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        print("Final Balance=",self.__balance)
'''class Bank(BankAccount):
    def display(self):
        print(self.__balance)'''

b1=BankAccount(10000)
b1.deposit(5000)
b1.withdraw(2000)
b1.get_balance()
b2=Bank(1000)
b2.display()