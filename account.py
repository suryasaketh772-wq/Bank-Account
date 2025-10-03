class BankAccount:
    def __init__(self,name,account_no,ifsc_code,balance=0):
        self.name=name
        self.account_no=account_no
        self.ifsc_code=ifsc_code
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Deposited amount {amount} New balance {self.balance}"
        else:
            return "invalid amount"
                
    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            return f"withdraw amount {amount} new balance {self.balance}"
        else:
            return "insufficeint balance"
            
            
    def balance_enquiry(self):
        return f"name:{self.name}\naccount_number:{self.account_no}\nifsc_code:{self.ifsc_code}\nbalance={self.balance}"
        
bank=BankAccount("surya",1234567890,"SBIN758484",500)
print(bank.balance_enquiry())
print(bank.withdraw(200))
print(bank.deposit(3001))
            
            
            