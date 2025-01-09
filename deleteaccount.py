def delete_account(accounts, logged_in_account=None):
    if logged_in_account and logged_in_account["account_type"] == "normal":
        confirm = input(f"Are you sure you want to delete your account, {logged_in_account['name']}? (y/n): ").lower()
        if confirm == "y":
            accounts.remove(logged_in_account)
            print("Account deleted successfully.")
            return True
        else:
            print("Account deletion cancelled.")
            return False
    else:
        if not accounts:
            print("No accounts available to delete.")
            return

        print("\nAvailable accounts:")
        for idx, account in enumerate(accounts):
            print(f"{idx + 1}. Name: {account['name']}, Type: {account['account_type']}")

        try:
            choice = int(input("Enter the number of the account you want to delete: ")) - 1
            if 0 <= choice < len(accounts):
                confirm = input(f"Are you sure you want to delete the account of {accounts[choice]['name']}? (y/n): ").lower()
                if confirm == "y":
                    deleted_account = accounts.pop(choice)
                    print(f"Account {deleted_account['name']} deleted successfully.")
                else:
                    print("Account deletion cancelled.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
