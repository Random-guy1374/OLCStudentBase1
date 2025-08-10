firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")

username = firstname[0:3] + lastname

print("Your username is " + username)

password = input("Please enter a password: ")
while True:
    if len(password) < 8:
        password = input("Password must be atleast eight characters\nPlease enter a password again: ")
    else:
        break

password_2 = input("Please confirm your password: ")
while True:
    if password != password_2:
        password_2 = input("Password entries do not match. Please repeat the second entry of your password: ")
    else:
        print("Your password has been set")
        break