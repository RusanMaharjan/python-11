import random
# Bank Class
class Bank:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
        self.account_number = "".join(str(random.randint(0, 9)) for i in range(16))

    # Deposit Function   
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('-'*55)
            print(f'Amount Rs.{amount} deposited to A/C {self.account_number}.')
            print('-'*55)
        else:
            print('-'*55)
            print(f'Deposit amount must be greater than 0.')
            print('-'*55)

    # Withdraw Function
    def withdraw(self, amount):
        if amount < self.balance:
            if amount % 1000 == 0:
                self.balance -= amount
                print('-'*55)
                print(f'Rs.{amount} has been withdrawn from A/C {self.account_number}.')
                print('-'*55)
            else:
                print('-'*55)
                print(f'Amount must be multiple of 1000.')
                print('-'*55)
        else:
            print('-'*55)
            print(f'Withdraw amount must be lower than balance amount.')
            print('-'*55)

    # Print user Details
    def print_details(self):
        print('-'*55)
        print('Account Details')
        print('-'*30)
        print(f'Account Name: {self.account_name}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Balance: Rs.{self.balance}')
        print('-'*55)