def login(accounts):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for account in accounts:
            if account["name"] == username and account["password"] == password:
                print(f"Login successful! Welcome, {username}.")
                return account

        print("Invalid username or password. Please try again.")
