def withdraw_money(account):
    while True:
        try:
            withdraw_amount = float(input("Enter the amount you want to withdraw: "))
            
            if withdraw_amount <= 0:
                print("Error: Withdrawal amount must be greater than zero. Please try again.")
                continue 
            
            if withdraw_amount > account['balance']:
                print(f"Error: Insufficient funds. Your balance is ${account['balance']:.2f}. Please try again.")
                continue  
            
            account['balance'] -= withdraw_amount
            account['transactions'].append({'type': 'Withdrawal', 'amount': withdraw_amount})
            
            print(f"Withdrawal of ${withdraw_amount:.2f} successful. New balance: ${account['balance']:.2f}")
            break  
        
        except ValueError:
            print("Error: Please enter a valid numeric value. Try again.")
