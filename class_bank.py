class Bank:
    def __init__(self,num=0,n='guest',t='normal',b=0):
        self.number=num
        self.name=n
        self.type=t
        self.balance=b
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Account number:",self.number)
        print("\n Name=",self.name)
        print("\n type=",self.type)
        print("\n Balance=",self.balance)
 

s = Bank(101,"Anu","Current Account",10000)
s.deposit()
s.withdraw()
s.display()
