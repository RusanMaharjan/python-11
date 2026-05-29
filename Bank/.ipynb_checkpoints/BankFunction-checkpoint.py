all_accounts = []
def findAccountByAccountNumber(acc_number):
    for data in all_accounts:
        if acc_number == data.account_number:
            return data
    return None