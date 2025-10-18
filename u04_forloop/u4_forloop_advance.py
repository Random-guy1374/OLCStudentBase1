
###########################################################
# Part 3. IN-CLASS Practice Exercises For loops
#
# Focus: Python for-loops (range, strings, lists, dicts, indexes)
###########################################################


#------------------------------------------------------------
# Exercise 1: Count Up with range(stop)
# Print the numbers 0 to 9 
# Use: range(10)
# Bonus Challenge: Print on one line, separated by spaces.

# Example: Output = 0 1 2 3 4 5 6 7 8 9
print("Exercise 1")
for i in range(10):
    print(i)
for i in range(10):
    print(i, end = " ")
print("\n")




#------------------------------------------------------------
# Exercise 2: Count Down with range(start, stop, step)
# Print 10 down to 1 
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 10 9 8 7 6 5 4 3 2 1
print("Exercise 2")
for index in range(10,0,-1):
    print(index, end = " ")
print("\n")





#------------------------------------------------------------
# Exercise 3: Evens in a Range
# Print all even numbers from 2 to 20.
# Bonus Challenge: Print on one line, separated by spaces.
# Example: Output = 2 4 6 8 10 12 14 16 18 20
print("Exercise 3")
for j in range(10):
    n = j + 1
    print(2*n, end = " ")
print("\n")
for j2 in range(2,21,2):
    print(j2, end = " ")
print("\n")





#------------------------------------------------------------
# Exercise 4: Multiples with Steps
# Print the first 6 multiples of 9.
# Use: range(start, stop, step) where step = 9
# Tip: Think about where to stop so you get 6 numbers.
# Example: Output = 9 18 27 36 45 54
print("Exercise 4")
for i2 in range(9,7*9,9):
    print(i2, end = " ")
print("\n")




#------------------------------------------------------------
# Exercise 5: Running Total (Accumulator)
# Compute the sum of all integers from 1 to 100 (inclusive) and print it.
# Use: range(1, 101)
# Example: Output = 5050
print("Exercise 5")
total = 0
for i3 in range(1,101):
    total += i3
    # print(total)
print(total)
print("\n")




#------------------------------------------------------------
# Exercise 6: Sum of Multiples
# Compute the sum of multiples of 3 from 3 to 30 (inclusive).
# Use: range(3, 31, 3)
# Example: Output = 165
print("Exercise 6")
total2 = 0
for i4 in range(3, 31, 3):
    total2 += i4
    # print(total)
print(total2)
print("\n")



#------------------------------------------------------------
# Exercise 7: Loop Through a String (characters)
# Count the vowels in the string and print the total.
# Data:
# text = "Computhink Academy"
# Vowels: a, e, i, o, u (case-insensitive)
# Example: Output = 7


# print("Exercise 7")
# count = 0
# text = input("Enter a text: ")
# for i5 in range(len(text)):
#     if text[i5].lower() in ["a","e","i","o","u"]:
#     # if "a" == text[i5].lower() or "i" == text[i5].lower() or "i" == text[i5].lower() or "o" == text[i5].lower() or "u" == text[i5].lower():
#         count += 1 
# print("Output :",count)
# print("\n")




#------------------------------------------------------------
# Exercise 8: Loop Through a String Using Index
# Print each character with its index in the format: index:char
# Data:
# name = "Python"
# Example: 
# 0:P
# 1:y
# 2:t
# 3:h
# 4:o
# 5:n


# print("Exercise 8")
# count = 0
# name = input("Enter a name: ")
# for char in range(len(name)):
#     print(char,":",name[char])
# print("\n")




#------------------------------------------------------------
# Exercise 9: Every 2nd Character (Index Step)
# Print every 2nd character (positions 0, 2, 4, ...) of the string on one line (no spaces).
# Data:
# s = "abcdefghijkl"
# Example: Output = acegik


# print("Exercise 9")
# the_text = ""
# s = input("Enter : ")
# for i6 in range(0,len(s),2):
#     the_text += s[i6]
# print(the_text)
# print("\n")






#------------------------------------------------------------
# Exercise 10: Loop Through a List (values)
# Print the squares of all numbers in the list on one line, separated by spaces.
# Data:
# nums = [3, 1, 4, 1, 5, 9]
# Example: Output = 9 1 16 1 25 81
print("Exercise 10")
nums = [3, 1, 4, 1, 5, 9]
new_nums = []
for i7 in range(len(nums)):
    new_nums += [nums[i7]**2]
for i7 in range(len(new_nums)):
    print(new_nums[i7], end = " ")
print("\n")




#------------------------------------------------------------
# Exercise 11: Loop Through a List Using Index
# Replace every negative number in the list with 0, then print the updated list.
# Data:
# data = [5, -2, 7, -9, 0, 4]
# Expected final list: [5, 0, 7, 0, 0, 4]


print("Exercise 11")
data = [5, -2, 7, -9, 0, 4]
for i8 in range(len(data)):
    if data[i8] <= 0:
        data[i8] = 0
print(data)
print("\n")




#------------------------------------------------------------
# Exercise 12: Manual Max (No max())
# Find and print the largest number in the list without using max().
# Data:
# scores = [42, 67, 23, 88, 55, 88, 12]
# Example: Output = 88
print("Exercise 12")
scores = [42, 67, 23, 88, 55, 88, 12]
highest = 0
for i9 in range(len(scores)):
    if highest <= scores[i9]:
        highest = scores[i9] 
print("The highest :",highest)
print("\n")




#------------------------------------------------------------
# Exercise 13: Loop through a List (index + value)
# Print each item with a 1-based index like "1) apple", "2) banana", ...
# Data:
# fruits = ["apple", "banana", "cherry", "durian"]
print("Exercise 13")
fruits = ["apple", "banana", "cherry", "durian"]
for i10 in range(len(fruits)):
    print(fruits[i10],",",i10+1)
print("\n")





#------------------------------------------------------------
# Exercise 14: Pair Two Lists 
# Print "Alice: 85", "Ben: 73", etc. by pairing names with marks.
# Data:
# names = ["Alice", "Ben", "Carmen", "Dylan"]
# marks = [85, 73, 91, 66]
print("Exercise 14")
names = ["Alice", "Ben", "Carmen", "Dylan"]
marks = [85, 73, 91, 66]
for i11 in range(len(names)):
    print(names[i11],end = ": ")
    print(marks[i11], end = ", ")
print("\n")




#------------------------------------------------------------
# Exercise 15: Nested Loops – Times Table
# Print a 1–5 multiplication table with rows like:
# 1 2 3 4 5
# 2 4 6 8 10
# ...
# Use two for-loops (outer row 1..5, inner col 1..5).
print("Exercise 15")
for index1 in range(1,6):
    print(index1, end = " ")
    for index2 in range(1,6):
        print(index2+index1, end = " ")
    print("\t")




#------------------------------------------------------------
# Exercise 16: Pattern Printing (Right Triangle)
# For n = 5, print:
# *
# **
# ***
# ****
# *****
# Use a for-loop and string multiplication.
print("Exercise 16")
star = "*"
for index3 in range(6):
    for index4 in range(index3+1):
        print(star,end = "")
    print("\t")
print("\n")




#------------------------------------------------------------
# Exercise 17: Dictionary Iteration (keys & values)
# Print "Alice : 72" etc. for each pair in the dict.
# Data:
# grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}
print("Exercise 17")
grades = {"Alice":72, "Ben":65, "Chloe":88, "Dion":55}

for name1, mark1 in grades.items():
    print(name1,end = ": ")
    print(mark1)
print("\n")





#------------------------------------------------------------
# Exercise 18: Dictionary Aggregation
# Compute and print the average value in the dictionary (to 1 decimal place).
# Data:
# temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}
# Example: Output = 30.9
print("Exercise 18")
temps = {"Mon":31.2, "Tue":29.8, "Wed":30.5, "Thu":32.0, "Fri":31.0}
total_temp = 0
for date, temp in temps.items():
    total_temp += temp
avg_temp = total_temp/len(temps)
print("Average tempurature: ",avg_temp)
print("\n")




#------------------------------------------------------------
# Exercise 19: Filter from a Dictionary
# Print only the students who passed (score >= 50) in "Name (score)" format.
# Data:
# results = {"Amy":49, "Bao":77, "Chin":50, "Deepa":92, "Eun":38}
# Example:
# Bao (77)
# Chin (50)
# Deepa (92)
print("Exercise 19")
results = {"Amy":49, "Bao":77, "Chin":50, "Deepa":92, "Eun":38}
for name2, mark2 in results.items():
    if mark2 >= 50:
        print(name2,end = ": ")
        print(mark2)
print("\n")



#------------------------------------------------------------
# Exercise 20: for-else Search
# Search for target in the list; print "Found at index i" or "Not found".
# Use for-else (else runs only if loop completes with no break).
# Data:
# items = ["id-001", "id-007", "id-010", "id-013"]
# target = "id-010"


# print("Exercise 20")
# items = ["id-001", "id-007", "id-010", "id-013"]
# target = input("Enter Target: ")
# if target in items:
#     for index6 in range(len(items)):
#         if target == items[index6]:
#             print("Found at index",index6+1)
        
# else:
#     print(target,"is not found")
# print("\n")




#------------------------------------------------------------
# Exercise 21: Skip and Stop (continue / break)
# Loop through the string:
#  - Skip vowels (do not print them).
#  - Stop printing entirely if you meet an exclamation mark '!' (break).
# Data:
# msg = "Code smarter, not harder!"
# Expected printed output (no vowels, stop at '!'): Cd smtr, nt hrdr


# print("Exercise 21")
# message = input("Enter: ")
# string = ""
# for index7 in range(len(message)):
#     if message[index7] == "!":
#         break
#     if (message[index7].lower() in ["a","e","i","o","u"]) == False:
#         string = string + message[index7]
# print(string)
# print("\n")




#------------------------------------------------------------
# Exercise 22: Character Frequency (build a dict)
# Build and print a frequency dictionary {char: count} for letters only (ignore spaces).
# Treat uppercase and lowercase as the same.
# Data:
# line = "Better code, better life"
# Example (order may vary): {'b':2, 'e':6, 't':4, 'r':2, 'c':1, 'o':1, 'd':1, 'l':1, 'i':1, 'f':1}


print("Exercise 22")
letter_dict = {}
line = "Better code, better life"
line = line.lower()
# line = input("Enter: ").lower()
for char2 in line:
    print(char2)
    if (char2 not in letter_dict) and char2.isalpha() == True:
        letter_dict[char2] = 0
    if char2.lower() in letter_dict: 
        letter_dict[char2] += 1
    
print(letter_dict)
print("\n")





#------------------------------------------------------------
# Exercise 23: Index Windows (String Slices by Loop)
# Print every 3-letter chunk of the string using indexes (i, i+3).
# Ignore the leftover if length is not a multiple of 3.
# Data:
# dna = "ATGCGATACGCTTGA"
# Example:
# ATG
# CGA
# TAC
# GCT
# TGA

print("Exercise 23")
letter_dict = {}
# line = "Better code, better life"
# line = line.lower()
line = input("Enter: ").lower()
for char2 in line:
    print(char2)
    if (char2 not in letter_dict) and char2.isalpha() == True:
        letter_dict[char2] = 0
    if char2.lower() in letter_dict: 
        letter_dict[char2] += 1
    
print(letter_dict)
print("\n")





#------------------------------------------------------------
# Exercise 24: Two-List Computation 
# Given costs and quantities, print "Item i: $TOTAL" per line and the grand total.
# Data:
# costs = [1.20, 0.80, 3.50, 2.00]
# qty   = [3,     5,    2,    1   ]
# Example lines:
# Item 1: $3.60
# Item 2: $4.00
# Item 3: $7.00
# Item 4: $2.00
# Grand Total: $16.60





#------------------------------------------------------------
# Exercise 25: Validate with for-loop (All Digits)
# Check if a string consists only of digits (0–9) using a for-loop.
# You cannot use .isdigit()
# Data:
# token = "A12345"
# Print True or False accordingly (no .isdigit()).





#------------------------------------------------------------
# Exercise 26: Build a New List 
# From the list, build a new list containing only the positive even numbers, then print it.
# Data:
# nums = [-3, -2, 0, 1, 2, 3, 4, 11, 12]
# Expected: [2, 4, 12]


#------------------------------------------------------------
