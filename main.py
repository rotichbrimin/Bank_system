
import storage

from accounts import create_account, delete_account
from transactions import deposit, withdraw, transfer_money
from queries import view_balance, view_accounts, search_account, view_transactions
from auth import change_pin



          

 
accounts =storage.load_data()
while True:
    print("\n=== MENU ===")
    print("1. Add Account: ")
    print("2. Deposit: ")
    print("3. Withdraw: ")
    print("4. View Balance: ")
    print("5. Transfer Money: ")
    print("6. View Accounts: ")
    print("7. Delete Account: ")
    print("8. Search Account: ")
    print("9. Change pin: ")
    print("10. View Transactions: ")
    print("11. Exit: ")
    
    try:
        option = int(input("\nChoose an option: "))
        
        if option == 1:
            while True:
                accounts.append(create_account(accounts))
                storage.save_data(accounts)
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
            change_pin(accounts)
        elif option == 10:
            view_transactions(accounts)
        elif option == 11:
            break
        else:
            print("Enter a valid option (1,2,3,4,5,6,7,8)")
    except ValueError:
        print("Enter a valid option:")
        continue
            
            