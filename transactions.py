def transactions_list(account):
    if not account['transactions']:
        print("No transactions available.")
    else:
        print(f"Transaction Statement for {account['name']}:")
        for transaction in account['transactions']:
            print(transaction)
