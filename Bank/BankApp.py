from BankClass import Bank
from BankFunction import all_accounts, findAccountByAccountNumber

def bankApp():
    try:
        while True:
            print(f'\nWelcome To Bank Application')
            print('1. Create Account')
            print('2. Deposit Balance')
            print('3. Withdraw Balance')
            print('4. Show Details')
            print('5. Exit')
        
            choice = int(input('Enter your choice: '))
        
            if choice == 1:
                name = input('Enter your account name: ')
                amount = int(input('Enter your initial balance: '))
        
                if amount >= 500:
                    b = Bank(name, amount)
                    all_accounts.append(b)
                    print('-'*55)
                    print(f'Account created with {name} with A/C {b.account_number}.\nRs.{amount} deposited to A/C {b.account_number}.')
                    print('-'*55)
                else:
                    print('Initial balance must be more or equals to Rs.500.')
            elif choice == 2:
                account = input('Enter your account number: ')
                find_acc = findAccountByAccountNumber(account)
                if find_acc:
                    balance = int(input('Enter your deposit balance: '))
                    find_acc.deposit(balance)
                else:
                    print(f'No account found!!')
            elif choice == 3:
                account = input('Enter your account number: ')
                find_acc = findAccountByAccountNumber(account)
                if find_acc:
                    balance = int(input('Enter your withdraw balance: '))
                    find_acc.withdraw(balance)
                else:
                    print(f'No account found!!')
            elif choice == 4:
                account = input('Enter your account number: ')
                find_acc = findAccountByAccountNumber(account)
                if find_acc:
                    find_acc.print_details()
                else:
                    print('No account found!!')
            elif choice == 5:
                print(f'Thank You for Choosing Us.')
                break
            else:
                print('Invalid Input.')
    except ValueError:
        print(f'Only number integer values are allowed!!')