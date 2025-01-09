def transfer_money(sender_account, accounts):
    while True:
        try:
            receiver_name = input("Enter the name of the account to transfer to: ")
            transfer_amount = float(input("Enter the amount to transfer: "))

            if transfer_amount <= 0:
                print("Transfer amount must be greater than zero. Please try again.")
                continue
            if transfer_amount > sender_account['balance']:
                print(f"Insufficient balance. Your balance is ${sender_account['balance']:.2f}.")
                continue

            receiver_account = next((acc for acc in accounts if acc['name'] == receiver_name), None)
            if not receiver_account:
                print("Receiver account not found. Please check the name and try again.")
                continue

            sender_account['balance'] -= transfer_amount
            receiver_account['balance'] += transfer_amount

            sender_account['transactions'].append({
                "type": "Transfer",
                "amount": transfer_amount,
                "details": f"To {receiver_name}"
            })
            receiver_account['transactions'].append({
                "type": "Transfer",
                "amount": transfer_amount,
                "details": f"From {sender_account['name']}"
            })

            print(f"Transfer of ${transfer_amount:.2f} to {receiver_name} successful.")
            break

        except ValueError:
            print("Invalid input. Please enter a valid number for the transfer amount.")
