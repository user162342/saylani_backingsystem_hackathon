import uuid

def create_account():
    while True:
        try:
            user_name = input("Enter name: ")

            user_password = input("Set your password: ")
            if not user_password:
                print("Password cannot be empty. Please try again.")
                continue

            user_age = input("Enter age: ")
            if not user_age.isdigit():
                print("Age must be a valid number. Please try again.")
                continue
            user_age = int(user_age)
            if user_age <= 0:
                print("Age must be a positive number. Please try again.")
                continue

            user_initial_balance = input("Enter balance: ")
            try:
                user_initial_balance = float(user_initial_balance)
                if user_initial_balance < 0:
                    print("Initial balance must be zero or greater. Please try again.")
                    continue
            except ValueError:
                print("Balance must be a valid number. Please try again.")
                continue

            account_type = input("Enter account type (normal/admin): ").lower()
            if account_type not in ["normal", "admin"]:
                print("Invalid account type. Please choose 'normal' or 'admin'.")
                continue

           
            account_id = str(uuid.uuid4()) 

            account = {
                "id": account_id, 
                "name": user_name,
                "password": user_password,
                "age": user_age,
                "balance": user_initial_balance,
                "transactions": [],
                "account_type": account_type,
            }
            return account

        except ValueError:
            print("Invalid input. Please enter valid values for age and balance.")
