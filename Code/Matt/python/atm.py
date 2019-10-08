class ATM:
    def __init__(self,balance,intrest):
        self.balance = balance
        self.intrest = intrest

    def check_balance(self):
        return self.balance

    def deposit (self,amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self,amount):
        return self.balance >= amount



    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


    def calc_intrest(self):
        self.intrest * self.balance
        return self.intrest



atm1 = ATM(50 , .1)
# print(atm1.deposit(55))
print(atm1.check_balance())
print(atm1.check_withdrawal(60))
print(atm1.withdraw(30))
print(atm1.calc_intrest())
