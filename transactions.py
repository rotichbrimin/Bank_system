
import storage
from auth import verify_pin


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
                        acc['transactions'].append(f"Deposited KSH: {amount}")
                        storage.save_data(accounts)
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
                        acc['transactions'].append(f"Withdrew KSH: {amount}")
                        storage.save_data(accounts)
                        print(f"KSH: {amount} withdrawn successfully fom ACC: {account_number} ")
                        print(f"New balance: {acc['balance']}")
                        return
                    
            if not found:
                print("Account number not found! ")
                continue
                    
        except ValueError:
            print("Enter a valid account number! ")
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
            
        if not verify_pin(sender_acc):
            print("Access denied! ")
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
        sender_acc['transactions'].append(f"Sent KSH: {amount} to {receiver}")
        receiver_acc['balance'] += amount
        receiver_acc['transactions'].append(f"Received KSH: {amount} from {sender}")
        storage.save_data(accounts)
        print(f"KSH: {amount} transferred from {sender} to {receiver} successfully! ")
        break             