###########################################################
# Part 2. IN-CLASS Practice Exercises
# Exercise 7: Multiplication Table with While Loop
# Write a program to print the multiplication table of 7 up to 10.
# Example: 7 x 1 = 7, ..., 7 x 10 = 70.
print("Exercise 7: Multiplication Table with While Loop")
i = 1
while i<= 10:
    print(f"7 x {i} = {7*i}")
    i = i + 1




#------------------------------------------------------------
# Exercise 8: Sum of Even Numbers
# Write a program to calculate the sum of even numbers between 1 
# and 20 using a while loop. Example: Output = 110.
print("\nExercise 8: Sum of Even Numbers")
i = 1
total = 0
while i <= 20:
    if i%2 == 0:
        total =  total + i
    i = i + 1
print(total)



#------------------------------------------------------------
# Exercise 9: Guessing Game
# Write a program where the user has to guess a random number 
# between 1 and 10. Keep prompting until they guess correctly.

print("\nExercise 9: Guessing Game")
import random
number = int(input("Enter a number from 1 to 10 : "))
random_number = random.randint(1,10)
while number != random_number:
    number = int(input("Enter a number from 1 to 10 : "))
    # print(number)
    # print(random_number)





#------------------------------------------------------------
# Exercise 10: Input Validation for a Password
# Write a program that keeps asking the user to enter a password.
# If the password is correct, print "Access granted."

print("\nExercise 10: Input Validation for a Password")
correct_password = "cheeseburger"
password = input("Enter  password : ")
while password != correct_password:
    password = input("Enter  password : ")





#------------------------------------------------------------
# Exercise 11: Printing Fibonacci Sequence
# Write a program to print the first 10 numbers in the Fibonacci
# sequence using a while loop. The Fibonacci sequence is a series 
# of numbers where each number is the sum of the two preceding 
# ones. It starts with 0 and 1.
# Example: Output = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

print("\nExercise 11: Printing Fibonacci Sequence")
a = 0
b = 1
i = 0
while i < 20:
    print(a,b)
    a = a + b
    b = b + a  
    i = i + 4






#------------------------------------------------------------
# Exercise 12: Custom Pattern
# Write a program to print the following pattern:
# *
# **
# ***
# ****
# *****

print("\nExercise 12: Custom Pattern")
dot = "*"
i = 0
while i <= 5:
    print(dot*i)
    i += 1   




#------------------------------------------------------------