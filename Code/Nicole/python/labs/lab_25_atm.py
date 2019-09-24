# atm.py

class Atm:
    def __init__(self, balance = 0, int_rate = 0.1):
        self.balance = float(balance)
        self.int_rate = float(int_rate)
        
    def check_balance(self):
        return self.balance
        
    def deposit(self, amount):
        amount = int(amount)
        self.balance += amount
        return self.balance
    
    def check_withdrawal(self, amount):
        return self.balance >= amount
    
    def withdraw(self, amount):
        amount = int(amount)
        self.balance -= amount
        return self.balance
    
    def calc_interest(self):
        pass
    
    def print_transactions(self, transaction):
        pass
        

my_atm = Atm()
print(f"\nYour beginning balance is: ${my_atm.balance}")
transactions = []

while True:
    if my_atm.balance >= 0:
        user_question = input("\nTo check your BALANCE, type 1.\nTo make a DEPOSIT, type 2.\nTo make a WITHDRAWAL, type 3.\nTo EXIT, type 4.\n\n")
        if user_question == "1":
            print(f"\nYour balance is ${my_atm.balance}")
        elif user_question == "2":
            user_deposit = input("\nHow much would you like to deposit? ")
            print(f"\nYour account balance is now ${my_atm.deposit(user_deposit)}")
            transactions.append(f"User deposited ${user_deposit}")
        elif user_question == "3":
            user_withdrawal = input("\nHow much would you like to withdrawal? ")
            user_withdrawal = int(user_withdrawal)
            if my_atm.check_withdrawal(user_withdrawal) is False:
                print("\nSorry, you don't have enough money to withdrawal that amount.")
            else:
                print(f"\nYour account balance is now ${my_atm.withdraw(user_withdrawal)}")
                transactions.append(f"User withdrew ${user_withdrawal}")
        elif user_question == "4":
            break
        user_question_3 = input("\nWould you like to make another transaction? ")
        if user_question_3 == "yes" or user_question_3 == "y":
            continue
        else:
            transactions = "\n".join(transactions)
            print(f"\nHere is your list of transactions from this session:\n{transactions}")
            break