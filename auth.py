import storage

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
            


def change_pin(accounts):
    if not accounts:
        print("No accounts available! ")     
        return
    while True:   
        try:
            acc_num = int(input("Enter account number: "))
        
            if acc_num <=0:
                print("Account number must be more than 0. Try again! ")
                continue
            if len(str(acc_num))!= 16:
                print("Account number musy be 16 digits. Try again!")
                continue
            for acc in accounts:
                if acc['account_number']== acc_num:
                    if not verify_pin(acc):
                        print("Access denied !")
                        return
                        
                    while True:
                        try:
                            new_pin = input("Enter new pin: ")
                            if not new_pin.isdigit() or len(new_pin) != 4:
                                print("Pin must be 4 digits! Try again! ")
                                continue
                                
                            acc['pin'] = int(new_pin)
                            storage.save_data(accounts)
                            print("New pin updated successfully! ")
                            return
                        except ValueError:
                            print("Enter a valid pin! ")
                            continue
                            
            print("Account not found")

        except ValueError:
            print("Enter a valid account number! ")
            continue