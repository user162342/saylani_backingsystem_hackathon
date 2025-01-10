# deleteaccount.py
def delete_account(accounts, logged_in_account=None):
    if logged_in_account:
        # If admin is logged in and wants to delete their own account
        if logged_in_account["account_type"] == "admin" and logged_in_account.get("admin_own_account_logged", False):
            confirm = input(f"Are you sure you want to delete your own admin account, {logged_in_account['name']}? (y/n): ").lower()
            if confirm == "y":
                accounts.remove(logged_in_account)
                print(f"Your admin account, {logged_in_account['name']}, has been deleted.")
                return True
            else:
                print("Account deletion cancelled.")
                return False

        # If admin wants to delete a non-admin account
        elif logged_in_account["account_type"] == "admin":
            print("\n--- Account List (excluding other admins) ---")
            non_admin_accounts = [account for account in accounts if account["account_type"] == "normal"]
            if not non_admin_accounts:
                print("No accounts available for deletion.")
                return False

            for i, account in enumerate(non_admin_accounts, 1):
                print(f"{i}. {account['name']} - {account['balance']}")

            try:
                account_to_delete_index = int(input("Enter the number of the account you want to delete: ")) - 1
                if account_to_delete_index < 0 or account_to_delete_index >= len(non_admin_accounts):
                    print("Invalid choice. Please try again.")
                    return False

                account_to_delete = non_admin_accounts[account_to_delete_index]
                confirm = input(f"Are you sure you want to delete {account_to_delete['name']}? (y/n): ").lower()

                if confirm == "y":
                    accounts.remove(account_to_delete)
                    print(f"Account {account_to_delete['name']} has been deleted.")
                    return False
                else:
                    print("Account deletion cancelled.")
                    return False

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return False

        # If not an admin, allow deletion of own account
        elif logged_in_account["account_type"] == "normal":
            confirm = input(f"Are you sure you want to delete your own account, {logged_in_account['name']}? (y/n): ").lower()
            if confirm == "y":
                accounts.remove(logged_in_account)
                print(f"Your account, {logged_in_account['name']}, has been deleted.")
                return True
            else:
                print("Account deletion cancelled.")
                return False
        else:
            print("Invalid account type.")
            return False
    else:
        print("No logged-in account provided for deletion.")
        return False
