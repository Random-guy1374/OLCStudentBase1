list_username = ["StudentNo1", "JaneJones", "ABC123"]


while True:
    username = input("Please enter a username: ")
    if username not in list_username:
        list_username.append(username)
        break
    else:
        print(f"{username} already existed")

while True:
    check1 = False

    password = input("Please enter a password: ")

    for char in password:
            if char.isdigit() == True:
                check1 = True
                break 
    
    if len(password) >= 8 and ("@" in password or "!" in password or "/" in password or "?" in password) and check1 == True:
        break
    else:
        if len(password) < 8:
            print("Password must contain at least 8 charaters")
        if "@" not in password and "!" not in password and "/" not in password and "?" not in password:
            print("Password must contains at least one special character from: @ ! / ?")
        if check1 == False:
            print("Password contains at least one numerical character")

    





    
