# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Printing Odd Numbers
# Write a program to print all odd numbers from 1 to 15.
# Use range(start, stop, step) to skip even numbers.
# Example: Output = 1, 3, 5, ..., 15.
print("Exercise 8: Printing Odd Numbers")
for i in range(1, 16, 2):
    print(i)


#------------------------------------------------------------
# Exercise 9: Multiplying Numbers
# Write a program to print the first 5 multiples of 7.
# Use range(start, stop, step).
# Example: Output = 7, 14, 21, 28, 35.
print("\nExercise 9: Multiplying Numbers")
for i in range(7, 36, 7):
    print(i)

#------------------------------------------------------------
# Exercise 10: Repeating a Phrase
# Write a program to print "I love Python!" 3 times.
# Use range(stop) to repeat the phrase.
print("\nExercise 10: Repeating a Phrase")
for i in range(3):
    print("I love Python!")



#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 5
# 44
# 333
# 2222
# 11111
print("\nExercise 11: Custom Counting Pattern")
for i in range(5, 0, -1):
    print(str(i)*(6-i))



#------------------------------------------------------------
# Exercise 12: Generating a Multiplication Table
# Write a program to print the multiplication table of 6.
# Example: 6 x 1 = 6, ..., 6 x 10 = 60.
print("\nExercise 12: Generating a Multiplication Table")
for i in range(11):
    print(f"6 x {i} = {6 * i}")



#------------------------------------------------------------
# Exercise 13: Printing a Custom Star Pattern
# Write a program to print the following pattern:
# *
# ***
# *****
# *******
# *********
print("\nExercise 13: Printing a Custom Star Pattern")
dot = "*"
for i in range(5):
    print(dot+dot*(2*i))