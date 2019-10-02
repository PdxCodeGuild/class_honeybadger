

class ATM:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.intr_rate = interest_rate
        self.transaction_list = []

    def __str__(self):
        return f'ATM\n Balance: {self.balance}\n Interest Rate: {intr_rate}'

    def check_balance(self):
        return f'your balance is {self.balance}'


    def deposit(self, value):
        self.balance += value
        self.transaction_list.append(f'you deposited {value}')

    def check_withdrawal(self, value):
       return self.balance >= value
    
   
    def withdraw(self, value):
        self.balance -= value
        self.transaction_list.append(f'you withdrew {value}')

    def print_transactions(self):
        return self.transaction_list

        


ATM1 = ATM(0.0, 0.1)
another_transa = "y"


while another_transa == "y":
    
    user_input = input("What would you like to do? deposit, withdraw, balance, history ").lower()
    if user_input == "deposit":
        value = float(input("How much? "))
        ATM1.deposit(value)
        print(ATM1.check_balance())
    
    elif user_input == "withdraw":
        value = float(input("How much? "))
        ATM1.withdraw(value)
        ATM1.print_transactions
    
    elif user_input == "balance":
        print(ATM1.check_balance())
    
    elif user_input == "history":
        print(ATM1.print_transactions())

    another_transa = input("Would you like to make another transaction? Y/N ").lower()
    while another_transa not in ["y", "n"]:
        another_transa = input("Would you like to make another transaction? Y/N ").lower()

    else:
        print
