
import json

def save_data(accounts):
    with open("/storage/emulated/0/accounts.json", "w") as file:
        json.dump(accounts, file, indent = 4)

def load_data():
    try:
        with open("/storage/emulated/0/accounts.json", "r") as file:
            return json.load (file)
    except FileNotFoundError:
        return []
def  create_account(accounts):
    while True:
        name = input("Enter your name: ")
        
        if not name:
            print("Name cannot be empty! Try again! ")
            continue
        else:
            break
            
    while True:
        try:
            acc_num = int(input("Enter account number (16 digits): "))
            if acc_num <= 0:
                print("Account number must be positive:")
                continue
            if len(str(acc_num)) != 16:
                print("Account number must be  16")
                continue
            exists = False
            for acc in accounts:
                if acc['account_number'] == acc_num:
                    exists = True
                    break
            if exists:
                print(f"This account number {acc_num} exists. Try again!")
                continue
            break
        except ValueError:
            print("Enter a valid account number: ")
            
    while True:
        try:
            pin = input("Create a pin (4 digits): ")
            
            if not pin.isdigit() or len(pin) != 4:
                print("Pin must be four digits: ")
                continue
            pin = int(pin)
            break
        except ValueError:
            print("Enter a valid pin: ")
            continue
                
                
           
    while True:
        try:
            start_balance = int(input("Enter your start balance:"))
            if start_balance <0:
                print("Start balance must be more than 0:") 
                continue
            else:
                break
        except ValueError:
            print("Enter a number:")
    
          

    return{ 
       "name":name,
       "account_number":acc_num,
       "balance":start_balance,
       "pin":pin
     }
       
       
def verify_pin(acc):
    attempts = 3
    while attempts > 0:
        try:
            entered = int(input("Enter pin: ")) 
            
            if entered == acc['pin']:
                print("Login successful! ")
                print(f"\nBalance: {acc['balance']}")
                return True
                
            else:
                attempts -= 1
                print(f"Wrong pin! Attempts left: {attempts} ")
                    
        except ValueError:
            print("Enter a valid pin! ")
    print("Access denied! Too many wrong attempts! ")
    return False
            
            
 
def deposit(accounts):
    while True:
        try:
            account_number = int(input("Enter account number to deposit: "))
            if account_number <= 0 :
                print("Account number must be more than 0:")
                continue
            if len(str(account_number))!=16:
                print("Account number must be 16. Tru again! ")
                continue
            found = False
            for acc in accounts:
                if acc['account_number']== account_number:
                    found = True
                    break
                    
            if found:
                while True:
                    try:
                        amount = int(input("Enter amount to deposit: "))
                        
                        if amount <= 0:
                            print("Amount cannot be 0 :")
                            continue
                        acc['balance'] += amount
                        save_data(accounts)
                        print(f"{amount} deposited to account number {account_number} successfully!")
                        break
                    except ValueError:
                        print("Enter a valid amount!")
                        continue
                  
            if not found:
                print("Account number not found! ")
                continue
        except ValueError:
            print("Enter a valid account number:")
            continue
                
def withdraw(accounts):
    while True:
        try:
            account_number = int(input("Enter account number: ")) 
            if account_number <=0:
                print("Account number must be more than 0 !") 
                continue
            if len(str(account_number)) != 16:
                print("Account number must be 16 digits. Try again! ")
                continue
            found = False
            for acc in accounts:
                if acc['account_number'] == account_number:
                    found = True
                    if not verify_pin(acc):
                        print("Access denied")
                        return
                        
                    while True:
                        try:
                            amount = int(input("Enter amount to withdraw: "))
                        except ValueError:
                            print("Enter a valid amount:")
                            continue
                        if amount<=0:
                            print("Amount must be more than 0! ")
                            continue
                        if acc['balance'] < amount:
                            print("Insufficient funds! ")
                            continue
                        acc['balance'] -= amount
                        save_data(accounts)
                        print(f"KSH: {amount} withdrawn successfully fom ACC: {account_number} ")
                        print(f"New balance: {acc['balance']}")
                        return
                    
            if not found:
                print("Account number not found! ")
                continue
                    
        except ValueError:
            print("Enter a valid account number! ")
            continue                
                

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
                    print(" === YOUR BALANCE ===")
                    print(f"Name: {acc['name']}")
                    print(f"Balance: {acc['balance']}")
                    
                if not found:
                    print(f"Account number {account_no} not found. Try again!")
                    continue
        except ValueError:
            print("Enter a valid accont number") 
            continue      

def transfer_money(accounts):
    while True:
        try:
            sender = int(input("Enter sender's account number: "))
            
            if sender <=0:
                print("Account number must be more than 0: ")
                continue
            if len(str(sender))!= 16:
                print("Account number must be 16 digits. Try again! ")
                continue
        except ValueError:
            print("Enter a valid account number. Try again! ")
            continue
        sender_acc = None
        for acc in accounts:
            if acc['account_number'] == sender:
                sender_acc = acc
                break
        if not sender_acc:
            print("Sender account not found! ")
            continue
        else:
            break
       
    while True:
        try:
            receiver = int(input("Enter receiver's account number: "))
            if receiver <=0:
                print("Account number must be more than 0 :")
                continue
            if len(str(receiver))!= 16:
                print(" Account number must be 16: ")
                continue
                
        except ValueError:
            print("Enter a valid account number. Try again! ")
        receiver_acc = None
        for acc in accounts:
            if acc['account_number'] == receiver:
                receiver_acc = acc
                break
                
        if not receiver_acc:
            print("Receiver account number not found. Try again: ")
            continue
        
        if sender == receiver:
            print("Cannot transfer to same account")
            continue
        
        try:
            amount = int(input("Enter amount to transfer: "))
            
            if amount <=0:
                print("Amount must be more than 0: ")
                continue
            if sender_acc['balance'] < amount:
                print("Insufficient funds: ")
                continue
                
        except ValueError:
            print("Enter a valid amount! ")
            continue
                
        sender_acc['balance'] -= amount
        receiver_acc['balance'] += amount
        save_data(accounts)
        print(f"KSH: {amount} transferred from {sender} to {receiver} successfully! ")
        break



def view_accounts(accounts):
    if not accounts:
        print("No accounts saved! ")
        return
     
    print("\n=== SAVED ACCOUNTS ===")
    for acc in accounts:
        print(f"\nName: {acc['name']} | Account Number: {acc['account_number']}")
        

def delete_account(accounts):
    while True:
        
        if not accounts:
            print("No account available to delete!")
            return
        
        try:
            acc_num = int(input("Enter account number to delete: "))
        
            if acc_num <= 0:
                print("Account number must be more than 0: ")
                found= False
                continue
            if len(str(acc_num)) != 16:
                print("Account number must be 16 digits: ")
                continue
        
           
            
            for i, acc in enumerate(accounts):
                if acc['account_number']==acc_num:
                    found =True
                    if found:   
                        confirm = input("Are you sure to delete this account? yes/y or no/n: ")
                        if confirm in ["yes", "y"]:
                            del accounts[i]
                            save_data(accounts)
                            print(f"Account {acc_num} deleted succesfully")
                            return
                        elif confirm in ["no", "n"]:
                            print("Cancelled deletion successfully")
                            return
                        else:
                            print("Enter yes/y or no/n !")
                            continue
            if not found:             
                print("Account not found. Try again! ")
                continue
               
                
        except ValueError:
            print("Enter a valid account number! ")
            continue

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
              

accounts = load_data()
while True:
    print("\n=== MENU ===")
    print("1. Add Account: ")
    print("2. Deposit: ")
    print("3. Withdraw: ")
    print("4. View Balance: ")
    print("5. Transfer Money: ")
    print("6. View Accounts: ")
    print("7. Delete Account: ")
    print("8. Searvh Account: ")
    print("9. Exit: ")
    
    try:
        option = int(input("\nChoose an option: "))
        
        if option == 1:
            while True:
                accounts.append(create_account(accounts))
                save_data(accounts)
                again = input("\nAdd another account? yes/y or no/n? ").lower().strip()
                if again in ["yes", "y"]:
                    continue
                elif again in ["no","n"]:
                    break
                else:
                    print("Enter yes/y or no/n: ")
                    continue
        elif option == 2:
            deposit(accounts)
        elif option == 3:
            withdraw(accounts)
        elif option == 4:
            view_balance(accounts)
        elif option == 5:
            transfer_money(accounts)
        elif option == 6:
            view_accounts(accounts)
        elif option == 7:
            delete_account(accounts)
        elif option == 8:
            search_account(accounts)
        elif option == 9:
            break
        else:
            print("Enter a valid option (1,2,3,4,5,6,7,8)")
    except ValueError:
        print("Enter a valid option:")
        continue
            
            