password = input("Enter a password : ")
while True:
    if len(password) < 8:
        print("Invalid password")
        password = input("Password too short\nEnter a password again : ")
    if password.isalpha() == True:
        print("Invalid password")
        password = input("Must contain a number\nEnter a password again : ")
    elif password.isdigit() == True:
        print("Invalid password")
        password = input("Must contain a letter\nEnter a password again : ")
    if password.upper() == password:
        print("Invalid password")
        password = input("Must contain lowercase letter\nEnter a password again : ")
    if password.lower() == password:
        print("Invalid password")
        password = input("Must contain uppercase letter\nEnter a password again : ")
    else:
        print("Valid password")
        break