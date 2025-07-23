class Bank_Account:
    Min_balance = 100
    
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self._balance += amount
            print(f"Updated balance for {self.name} is: {self._balance}")
            
    def withdraw(self,amount):
        if amount  <=0 :
            print("Withdrawl amount must be positive ")
        elif amount > self._balance :
            print("Insufficient funds !! You need to add funds to withdraw the available ones  ")
        else :
            self._balance-=amount
            print(f"updated balance is {self._balance}")
                
            
            
    
    @staticmethod
    def check_interest_rate(rate):
        if rate > 3:
            return "The interest rate is according to you."
        else:
            return "Sorry, the interest rate is not available for you."


person1 = Bank_Account("Subham", 500)
person1.deposit(200)
person2 = Bank_Account("Sujal", 499)
person2.withdraw(700)
person3 = Bank_Account("Ajaya", 888)
person3.check_interest_rate(4)
    
              

