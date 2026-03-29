

import storage
from auth import verify_pin

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
       "pin":pin,
       "transactions":[]
     }
     
     
     
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
        
           
            found = False
            for i, acc in enumerate(accounts):
                if acc['account_number']==acc_num:
                    found =True
                    if not verify_pin(acc):
                        print("Access denied! ")
                        return
                    confirm = input("Are you sure to delete this account? yes/y or no/n: ")
                    
                    if confirm in ["yes", "y"]:
                        del accounts[i]
                        storage.save_data(accounts)
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