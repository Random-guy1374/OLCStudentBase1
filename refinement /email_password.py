# firstname = input("Please enter your first name: ").lower()
# lastname = input("Please enter your last name: ").lower()
# email_id = firstname[:3] + lastname + "@example.com"
# print("Your email ID is " + email_id)

#task 2.1
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
email_id = firstname[0] + lastname[-3:]
print(email_id)

#task 2.2
email_id2 = email_id + "@gmail.com"
# print("emialid2",email_id2)
while True:
    email = input("Re-enter your email to confirm: ")
    if email == email_id2:
        break
    elif "@" not in email:
        print("@ is not found please")

#task 2.3
while True:
    password = input("Enter a password")
    if len(password) != 8:
        print("Password must contain exactly 8 characters")
    # elif password.islower() == True:
    #     print("Password must contain a uppercase letter")
    # elif password.isupper() == True:
    #     print("Password must contain a lowercase letter")
    else:
        break