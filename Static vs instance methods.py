class Bank_Account():
    MIN_BALANCE = 100

    def __init__(self, username, address, balance=0):
        self.username = username
        self.address = address
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.username}'s balance is {self._balance}")
        else:
            print("Deposit amount must be positive")

    @staticmethod
    def interest_rate(rate):
        return 0 <= rate <= 5


account1 = Bank_Account("ram", "ratnanagar", 450)


print(account1.username)  
print(account1.address)   
print(account1._balance)  

print(Bank_Account.interest_rate(3))  
print(Bank_Account.interest_rate(6))  