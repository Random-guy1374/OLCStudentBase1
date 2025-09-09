# Exercise 0: Modulus and Floor Division
# Write a program to calculate the modulus and floor division
# of two numbers. Example: 17 divided by 5.
num1 = 17
num2 = 5
modulus = num1 % num2
floor_div = num1 // num2
print("17 % 5 is:", modulus)
print("17 // 5 is:", floor_div)

#------------------------------------------------------------
# For Loops through List
#------------------------------------------------------------

# Exercise 1: Printing Items (Method 1)
# Given fruits = ["apple", "banana", "cherry"]
# Use a for loop to print each fruit directly.
# Output example:
# I like to eat apple.
# I like to eat banana.
# I like to eat cherry.
fruits = ["apple", "banana", "cherry"]
for i in range(3):
    print("I like to eat",fruits[i])




#------------------------------------------------------------
# Exercise 2: Printing Items (Method 2)
# Given the same fruits list
# Use for i in range(len(fruits)) to print the items.
# Output example:
# Fruit 1: apple
# Fruit 2: banana
# Fruit 3: cherry

for i in range(len(fruits)):
    print("Fruit ",i+1,":",fruits[i])



#------------------------------------------------------------
# Exercise 3: Numbers Greater than 50
# Given numbers = [12, 67, 45, 89, 23]
# Use a for loop to print only numbers greater than 50.
# Expected Output:
# 67
# 89
numbers = [12, 67, 45, 89, 23]
for i in range(len(numbers)):
    if numbers[i] > 50:
        print(numbers[i])





#------------------------------------------------------------
# Exercise 4: Mapping Students to Scores
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}
students_mark = {}
students = ["Ali", "Bala", "Cindy"]
marks = [55, 80, 62]
for i in range(len(students)):
    students_mark[students[i]] = marks[i]
print(students_mark)


#------------------------------------------------------------
# While Loop Validation
#------------------------------------------------------------

# Exercise 5: Length Check
# Keep asking user for a username until it has at least 5 characters.


# while True:
#     username = input("Enter a username: ")
#     if len(username) < 5:
#         print("Invalid. Username must be 5 characters or more. ")
#     else:
#         break





# ----------------------------------------------------------------

# Exercise 6: Numbers Only
# Keep asking user to enter age until input contains digits only.


# while True:
#     age = input("Enter an age: ")
#     if age.isdigit() != True:
#         print("Invalid. Age contains digits only. ")
#     else:
#         break





# ----------------------------------------------------------------

# Exercise 7: Uppercase Only
# Keep asking until user enters a code in uppercase letters only.


# while True:
#     text = input("Enter a code in uppercase letters only: ")
#     if text.isupper() != True:
#         print("Invalid. Code in uppercase letters only. ")
#     else:
#         break





# ----------------------------------------------------------------

# Exercise 8: Lowercase Only
# Keep asking until user enters an email in lowercase only.


# while True:
#     email = input("Enter an email in lowercase only: ")
#     if text.isupper() != True:
#         print("Invalid. Email in lowercase only. ")
#     else:
#         break




# ----------------------------------------------------------------

# Exercise 9: Password Validation
# Keep asking until user enters a password with length >= 8.


# while True:
#     password = input("Enters a password with length more than or equal 8: ")
#     if len(password) < 8:
#         print("Invalid. Password too short. ")
#     else:
#         break





# (a) Input and validation [5 marks]
# Write a function get_valid_number(base) that:
# •	Accepts a parameter base which can be 2 or 10.
# •	Repeatedly asks the user to enter a number in that base until a valid number is provided.
# •	Checks that:
# o	For base 2: input only contains characters 0 and 1.
# o	For base 10: input only contains digits 0–9 (treat the value as a non-negative integer).
# •	Returns the number string (no leading/trailing spaces).
# Hint: Use .strip() and validate all characters before returning.


def get_valid_number(base):
    while True:
        if base.isdigit() != True:
            base = input("Invalid. Parameter base must be a number.\nEnter a parameter base of 2 or 10 : ")
        else:
            break
    while True:
        number_base = []
        for i in range(len(base)):
            number_base.insert(-len(base),int(base[i]))
        if 0 in number_base or 1 in number_base or base.isdigit() == True:
            break
        else:
            base = input("Invalid. Parameter base binary or decimal.\nEnter a parameter base of 2 or 10 : ")
    return base

parameter = input("Enter a parameter base of 2 or 10 : ")
result =  get_valid_number(parameter)
print(parameter,"is valid")




# ----------------------------------------------------------------
# (b) Binary → Denary [6 marks]
# Write a function bin_to_den(binstring) that:
# •	Reverses the string so the least significant bit is processed first,
# •	Forms a place-value list [2**0, 2**1, …] matching the string length,
# •	Multiplies each bit by its positional weight and accumulates the total,
# •	Returns the denary integer.
# Example: bin_to_den("11111011") should return 251.


def bin_to_den(binstring):
    while True:
        if binstring.isdigit() != True:
            binstring = input("Invalid. Enter a number in binary : ")
        else:
            break
    total = 0
    bina = []
    length = len(binstring)
    for i in range(length):
        bina.insert(-length,int(binstring[i]))
        # print("list",i,bina)
    for j in range(length):
        total += (2**(j))*(bina[j])
        # print("toal",total)

    return total

num = input("Enter a number in binary : ")
output = bin_to_den(num)
print("denery :",output)


# ----------------------------------------------------------------

