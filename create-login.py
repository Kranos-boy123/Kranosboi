import string
import time

special = string.punctuation

_user = ""
_pass = ""

print("""
1. create account
2. login
3. exit           
""")

while True:
    # select an option
    create_account = input("Please enter the following to create an account: ")
    if create_account == "1":
        user = input("Enter your username(must be at least 8 characters): ")
        
        # checks if the password is strong enough
        if any(ch in special for ch in user) and len(user) >= 8:
            print(f"User created: {user}")
        else:
            print("Username must be at least 8 characters long and contain a special character.")
            continue
        
        # checks if the password is greater than 8    
        while True:
            password = input("Enter your password: ")
            if any(ps in special for ps in password) and len(password) >= 8:
                _user = user
                _pass = password
                print("Password created.")
                time.sleep(1)
                print("Account created successfully!")
                break
            else:
                print("must contain atleaset one special chracter and 8 characters long.")
                continue

    elif create_account == "2":
        # checks if the user input a non existing account
        if _user == "" or _pass == "":
            print("No account found. Please create an account first.")
            continue

        # login user
        while True:
            user = input("Enter your username: ")
            if user != _user:
                print("Invalid user")
            else:
                break
                
        # login password
        while True:
            password = input("Enter your password: ")
            if password != _pass:
                print("Invalid password")
            elif password == _pass:
                print("Login succesfull!.")
                time.sleep(0.5)
                print(f"\nHello {_user}")
                break
                    
            else:
                print("Invalid input")

    elif create_account == "3":
        time.sleep(0.6)
        print("Goodbyeeeeee!")
        break
    else:
        print("Invalid choices")

                

            
                
            



            
            

