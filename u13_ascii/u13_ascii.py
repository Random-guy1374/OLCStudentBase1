##############################################################
### ASCII ord() and chr() for password generation
##############################################################

# #Generate a Simple Password
# # Write a Python program that generates a random password of a given length 
#     using ASCII printable characters.
# # Example input: length = 8
# # Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# # HINT: ASCII printable characters range from 33 to 126

# Sample solution 

# import random

# length = 8
# password = ""
# for i in range(length):
#     x = chr(random.randint(33,126))
#     password += x
# print("The generate is", password)










# import random

# length = 8
# password = ""
# for i in range(length):
#     char = chr(random.randint(33, 126))  
#     password += char
# print(f"Generated password: {password}")


###########################################################
# Generate a Password with Specific Character Types
# Scenario 1: Corporate Password Policy - Basic Compliance
# One of your clients, a fintech company, has implemented a basic password policy. 
# All system-generated passwords must:
# - Be of a specific length
# - Include at least 1 uppercase letter, 1 lowercase letter, and 1 digit

# Your task: Write a Python program to generate such a password.
# Example: input = 8 → output = 'aB3xG2#1'

# HINT: Use ASCII:
# - Uppercase letters: 65-90
# - Lowercase letters: 97-122
# - Digits: 48-57


# Write and test your code here

# import random

# password = ""
# length = 8
# upper = chr(random.randint(65,90))
# lower = chr(random.randint(97,122))
# digit = chr(random.randint(48,57))

# password = upper + lower + digit
# for i in range(length-3):
#     upper = chr(random.randint(65,90))
#     lower = chr(random.randint(97,122))
#     digit = chr(random.randint(48,57))
#     order = random.randint(1,3)
#     if order == 1:
#         password += upper
#     elif order == 2:
#         password += lower
#     else:
#         password += digit
# print(password)





###########################################################
# Exclude Specific Characters in Password
#  Scenario 2: Readability-Enhanced Password Generator
# A logistics firm found that users often confuse similar-looking characters 
# (like 'l', '1', 'I', 'O', and '0') when reading out passwords over the phone.

import random

 


