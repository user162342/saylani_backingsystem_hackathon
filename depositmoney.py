def deposit_money(account):
    while True:
        try:
            deposit_amount = float(input("Enter the amount you want to deposit: "))
            
            if deposit_amount <= 0:
                print("Deposit amount must be greater than zero. Please try again.")
                continue  
            
            account['balance'] += deposit_amount
            account['transactions'].append(f"Deposit: ${deposit_amount:.2f}")
            
            print(f"Deposit of ${deposit_amount:.2f} successful. New balance: ${account['balance']:.2f}")
            break  
            
        except ValueError:
            print("Invalid input. Please enter a valid number. Try again.")
