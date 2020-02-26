class Calculator():
    def add(self,num1,num2):
        return num1 + num2

calsi = Calculator()
total = calsi.add(100,200)
print('total is ',total)

class Account():
    def __init__(self,name,email,mobile,addressproof):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.addressproof = addressproof
        self.accountno = 101
        self.balance = 0
        
    def deposit(self,actNo,amt):
        self.balance = self.balance +amt
        return self.balance
    
raghuact = Account("Raghu Prasad","prasadraghuks@gmail.com",9845547471,9987898) 
print('Account no ', raghuact.accountno) 
bal = raghuact.deposit(raghuact.accountno,100000)
print('Balance ',bal) 
 