def view_accounts(accounts):
    print("\nAvailable accounts:")
    for idx, account in enumerate(accounts):
        print(f"{idx + 1}. Name: {account['name']}, Balance: ${account['balance']:.2f}, Type: {account['account_type']}")

def admin_total_deposits(accounts):
    total = sum(account['balance'] for account in accounts)
    print(f"Total Deposits in Bank: ${total:.2f}")

def admin_total_accounts(accounts):
    print(f"Total Number of Accounts: {len(accounts)}")
