from auth import verify_pin


def view_balance(accounts):
    while True:
        try:
            account_no = int(input("Enter account number to view balance: " ))
            if account_no <=0:
                print("Account number must be more than 0: ")
                continue
            if len(str(account_no)) != 16:
                print("Account number must be 16 didgits: Try again! ")
                continue
            else:
                found = False
                for acc in accounts:
                    if acc['account_number'] == account_no:
                        found = True
                        break
                        
                if found:
                    if not verify_pin(acc):
                        print("Access denied! ")
                        return
                        
                    print("\n === YOUR BALANCE ===")
                    print(f"Name: {acc['name']}")
                    print(f"Balance: {acc['balance']}")
                    
                if not found:
                    print(f"Account number {account_no} not found. Try again!")
                    continue
        except ValueError:
            print("Enter a valid accont number") 
            continue      
            
   
   
def view_accounts(accounts):
    if not accounts:
        print("No accounts saved! ")
        return
     
    print("\n=== SAVED ACCOUNTS ===")
    for acc in accounts:
        print(f"\nName: {acc['name']} | Account Number: {acc['account_number']}")
        
        
        

def search_account(accounts):
    if not accounts:
        print("No account to saved: ")
        return
        
    while True:
        try:
            acc_num = int(input("Enter account number: "))
            found = False
            if acc_num <=0:
                print("Account number must be more than 0 :")
                continue
            if len(str(acc_num)) != 16:
                print("Account number must be 16 digits: ")
                continue
                    
            for acc in accounts:
                if acc['account_number'] == acc_num:
                    
                    found = True
           
                    print(f"Name: {acc['name']} | {acc['account_number']}")
                    break
            if not found:
                print("Account not found. Try again! ")
                continue            
                    
        except ValueError:
            print("Enter a valid account number! ")
            continue
            
            
           
def view_transactions(accounts):
    acc_num = int(input("Enter account number: "))

    for acc in accounts:
        if acc['account_number'] == acc_num:

            if not verify_pin(acc):
                print("Access denied")
                return

            if not acc['transactions']:
                print("No transactions found")
                return

            print("=== TRANSACTION HISTORY ===")
            for t in acc['transactions']:
                print(t)
            return

    print("Account not found")             
