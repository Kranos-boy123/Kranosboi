# functionable bank system
import string
import time as t
accounts = {}
balances = {}
def create_account():
    special = string.punctuation
    digits = string.digits
    while True:
        try:
            initial = int(input("Enter your initial deposit: "))
            if initial < 1000:
                print("You are not allowed to create an account, initial deposit must be 1000 and above..")
            else:
                break
        except ValueError:
            print("Please enter a money")

    while True:
        user = input("Enter your user: ")
        if len(user) < 8:
            print("User must be 8 characters long")           
        else:
            print(f"User '{user}' has been created")
            break

    while True:
        _password = input("Enter your password ")
        if any(ch in special for ch in _password) and any(dg in digits for dg in _password) and len(_password) >= 8:
            accounts[user] = _password
            balances[user] = initial
            print(f"Password '{_password}' has been set successfuly")
            t.sleep(1)
            print("Account created...")
            break
        else:
            print("Must be atleast 8 chracters long and contain any special characters")
def login():
    print("\nLogin:")
    while True:
        user = input("Enter your user name: ")
        if user not in accounts:
            print("Your account is not found")
        else:
            while True:
                password = input("Enter your password: ")
                if accounts[user] == password:
                    return user                   
                else:
                    print("Invalid password")
        again = input("Press enter to try again or any key to exit> ")
        if again != "":
            return None
        
def bank(username):
    while True:
        t.sleep(1)
        print(f"\nWelcome to BDS bank '{username}'")
        print("=" * 40)
        print("1. Withdraw | 2. Deposit | 3. View Balance | 4. Logout")
        try:
            opt = input("Enter option: ")
            if opt == "4":
                print("Logging out.....")
                t.sleep(1.5)
                print(f"User '{username}' successfuly logged out")
                break
            elif opt == "3":
                print(f"Your balance: {balances[username]}")
            elif opt == "2":
                dep = int(input("Enter amount to deposit: "))
                if dep <= 0:
                    print("zero cannot be deposit!")         
                else:
                    print(f"Your balance: {balances[username]}")
                    balances[username] += dep
                    print(f"Updated balance: {balances[username]}")
            elif opt == "1":
                _withdraw = int(input("Enter amount of money to withdraw: "))
                if _withdraw < 0 or _withdraw < 100:
                    print("Must be 100 and above of money to withdraw")
                else:
                    balances[username] -= _withdraw
                    for i in balances.values():                    
                        print(f"Successfuly withdrawed: '{_withdraw}'")
                        print(f"Updated balance: {i}")
            else:
                print("Enter option above...")
        except ValueError:
            print("Please enter a valid input")
def main():
        while True:
            print("\nBDS bank: CEO John carl pogi")
            print("=" * 30)
            print("\n1. Create account | 2. Login | 3. Exit")
            opt1 = input("Enter option: ")
            match opt1:
                case "1":
                    create_account()
                case "2":
                    user = login()
                    if user:
                        bank(user)
                case "3":
                    print("Goodbye")
                    break
                    
if __name__ = "__main__":
    main()





