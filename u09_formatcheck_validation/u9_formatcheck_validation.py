# Part 2. IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").

print("Exercise 10: Validating Uppercase Input")

code = input("Enter a code : ")
while True:
    if code.isupper() != True:
        code = input("Code is not a uppercase\nEnter a code again: ")
    else:
        break




#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols.

print("\nExercise 11: Validating Alphanumeric Input")

username = input("Enter an username : ")
while True:
    if username.isalpha() != False or username.isdigit() != False:
        username = input("Username must only be alphanumeric characters\nEnter an username : ")
    else:
        break





#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.

print("\nExercise 12: Validating Numeric Input")

number = input("Enter a your phone number : ")
while True:
    if number.isdigit() != True:
        number = input("It is not a number\nEnter a your phone number again : ")
    else:
        break




#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.

print("\nExercise 13: Checking for Substrings")

word = input("Enter a sentence : ")

while True:
    if "Python" not in word:
        word = input("Python not found\n Enter a sentence again : ")
    else:
        break




#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").

print("\nExercise 14: Replacing Parts of a String")

gmail = input("Enter a gamil : ")

while True:
    if "@old.com" in gmail:
        gmail = gmail[:-8] + "@new.com"
        print(gmail)
    else:
        break



#------------------------------------------------------------