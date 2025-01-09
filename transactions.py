def transactions_list(account):
    if not account['transactions']:
        print(f"No transactions available for {account['name']}.")
    else:
        print(f"\nTransaction Statement for {account['name']}:")
        print("-" * 40)
        print("{:<25} {:>10}".format("Transaction Type", "Amount"))
        print("-" * 40)

        for transaction in account['transactions']:
            transaction_type = transaction['type']
            amount = transaction['amount']
            if transaction_type == "Transfer":
                detail = transaction.get('details', "")
                print(f"{transaction_type:<25} ${amount:.2f} - {detail}")
            else:
                print(f"{transaction_type:<25} ${amount:.2f}")
        
        print("-" * 40)
        print(f"Current Balance: ${account['balance']:.2f}")
