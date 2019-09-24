#Filename: autoteller.py

class atm:
    

    def __init__(self,balance,interest):
        self.balance = balance
        self.interest = interest
        self.translist = []
    
    def __str__(self):
        return f'atm:({self.balance},{self.interest})'

    def check_balance(self):
        return f'balance:({self.balance})'
    
    def deposit(self, amount):
        self.translist.append(f'{amount}, USD deposited')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.translist.append(f'{amount}, USD withdrawn')
        self.balance -= amount
        return self.balance

    def check_withdraw(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def calc_interest(self, time):
        self.interest = (self.balance * 0.01 * time)
        self.balance += self.interest
        return self.interest

    def print_transaction(self):
        return self.translist

acct = atm(100, 0.01)

# def transaction(acct):
#     amount = float(input('how much would you like to deposit?\n'))

#     print(acct.deposit(amount),acct.check_balance())

#     amount = float(input('how much would you like to withdraw?\n'))

#     if acct.check_withdraw(amount) == True:
#         print(acct.withdraw(amount),acct.check_balance())
#     else:
#         print('withdrawal denied due to lack of funds')

#     time = float(input('how much time has passed?\n'))

#     print('you have accumulated ',acct.calc_interest(time),' USD in interest')
#     print('your final balance is ',acct.check_balance(),' USD')
#     print(acct.print_transaction())

# transaction(acct)

def main(acct):
    myflag = True
    
    while myflag == True:
        
        selection = int(input('press 1 to check balance \n press 2 to make a withdrawal \n press 3 to make a deposit \n press 4 to exit\n'))
        
        if 0<selection<5:
            
            if selection == 1:
                print(acct.check_balance())
            
            elif selection == 2:
                amount = float(input('how much would you like to withdraw?\n'))
                if acct.check_withdraw(amount) == True:
                    acct.withdraw(amount)
                else:
                    print('withdrawal denied due to lack of funds')
            
            elif selection == 3:
                amount = float(input('how much would you like to deposit?\n'))
                acct.deposit(amount)
            
            elif selection == 4:
                print('your final balance is ',acct.check_balance(),' USD')
                print(acct.print_transaction())
                myflag = False
        
        else:
            print('invalid entry')

main(acct)



                

