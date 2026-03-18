# import random

# n = 0
# n2 = 4
# secret_code = ""
# secret_list = []
# for i in range(3):
#   digit = str(random.randint(1, 5))
#   secret_code = secret_code + digit


# while n < 5:
#     correct = 0
#     user_input = str(input("Guess the 3-digit number. Each digit is from 1 to 5: "))
#     for i2 in range(3):
#         if user_input[i2] == secret_code[i2]:
#             correct += 1
#     print(correct,"digits are correct and is/are in the right position")
#     n += 1
#     if correct == 3:
#        print("You get it",user_input,"is the secret code")
#        break
#     else:
#        print("You guess it wrong")
# if n == 5:
#    print("You did not get it in 5 tries the secret code is",secret_code)



import random

n = 0
n2 = 4
secret_code = ""
secret_list = []
for i in range(3):
    digit = str(random.randint(1, 5))
    secret_code = secret_code + digit

while n < 5:
    correct = 0
    while True:
        user_input = str(input("Guess the 3-digit number. Each digit is from 1 to 5: "))
        if len(user_input) != 3:
           print("Invalid number\nNumber must consist of only 3 digits")
        else:
           break
    for i2 in range(3):
        if user_input[i2] == secret_code[i2]:
            correct += 1
    print(correct,"digits are correct and is/are in the right position")
    n += 1
    if correct == 3:
       print("You get it",user_input,"is the secret code")
       break
    else:
       print("You guess it wrong")

if n == 5:
   print("You did not get it in 5 tries the secret code is",secret_code)