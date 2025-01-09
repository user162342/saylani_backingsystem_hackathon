from accounts import create_account
from checkbalance import check_balance
from depositmoney import deposit_money
from withdraw import withdraw_money
from transactions import transactions_list
from deleteaccount import delete_account
from viewaccounts import view_accounts, admin_total_deposits, admin_total_accounts
from login import login


def main():
    accounts = []

    while True:
        print("\nChoose what you want to do: ")
        print("1. Create an account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if not choice.isdigit() or int(choice) not in range(1, 4):
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        if choice == "1":
            new_account = create_account()
            if any(account['name'] == new_account['name'] for account in accounts):
                print("An account with this name already exists. Please choose a different name.")
            else:
                accounts.append(new_account)
                print("Account created successfully.")

        elif choice == "2":
            if not accounts:
                print("No accounts found. Please create an account first.")
                continue

            logged_in_account = login(accounts)

            if logged_in_account["account_type"] == "normal":
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. View Transactions")
                    print("5. Delete Account")
                    print("6. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        check_balance(logged_in_account)
                    elif user_choice == "2":
                        deposit_money(logged_in_account)
                    elif user_choice == "3":
                        withdraw_money(logged_in_account)
                    elif user_choice == "4":
                        transactions_list(logged_in_account)
                    elif user_choice == "5":
                        if delete_account(accounts, logged_in_account):
                            print("Your account has been deleted. Logging out...")
                            break  # Exit to the main menu after deleting the account.
                    elif user_choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif logged_in_account["account_type"] == "admin":
                while True:
                    print("\n1. View All Accounts")
                    print("2. Total Deposits")
                    print("3. Total Accounts")
                    print("4. Delete an Account")
                    print("5. Logout")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        view_accounts(accounts)
                    elif admin_choice == "2":
                        admin_total_deposits(accounts)
                    elif admin_choice == "3":
                        admin_total_accounts(accounts)
                    elif admin_choice == "4":
                        print("Deleting an account...")
                        delete_account(accounts)  # Admin can delete any account.
                    elif admin_choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting the system...")
            break
main()