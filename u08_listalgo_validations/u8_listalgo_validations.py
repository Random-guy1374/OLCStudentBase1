# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Finding the Smallest Without Built-In Functions
# Write a program to find the smallest number in a list without 
# using min().
print("Exercise 8: Finding the Smallest Without Built-In Functions")
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
smallest = numbers[0]
for num in numbers:
    if  num <= smallest:
        smallest = num
print("The smallest number is :",smallest)




#------------------------------------------------------------
# Exercise 9: Counting Occurrences of a Value
# Write a program to count how many times a specific number 
# appears in a list.
# Example: Input = [1, 2, 2, 3], Check for 2.

print("\nExercise 9: Counting Occurrences of a Value")

numbers = [1, 2, 2, 3, 2, 4, 2, 5, 2]

number_list = []
number = input("Enter a list of number e.g 1, 2, 2, 3 : ")
number_list = number.split(",")

count = 0
for i in number_list:
    if i == "2" or i == " 2":
        count += 1
print(f"There are {count} 2s")



#------------------------------------------------------------
# Exercise 10: Removing Duplicates from a List
# Write a program to remove duplicate values from a list.
# Example: Input = [1, 2, 2, 3, 4, 4], Output = [1, 2, 3, 4].

print("\nExercise 10: Removing Duplicates from a List")

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

emtry = []
number = input("Enter a list of number e.g 1,2,2,3,4,4: ")
number_list = number.split(",")
for i in number_list:
    if i not in emtry:
        emtry.append(i)
print(emtry)




#------------------------------------------------------------
# Exercise 11: Ensuring All Numbers Are Positive
# Write a program to check that all numbers in a list are 
# positive. If any number is negative, remove it and print the 
# updated list.

print("\nExercise 11: Ensuring All Numbers Are Positive")
numbers = [10, -5, 20, -15, 30, -25]

emtry = []
list = input("Enter a list : ")
number_list = list.split(",")

for i in number_list:
    if i not in emtry and float(i) >= 0:
        emtry.append(i)
print(emtry)

