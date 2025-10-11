# Paper 2 - 2025 O Level Computing
# Question for Task 2
word_list = ["apple", "window", "bend", "paper", "thought"]

# Task 2.1 [3]

# Extend the program to:
# - ask the user to input a new word
# - take the new word as input
# - convert the new word to lower case
# - store the new word at the end of the list in a new space

# You do not need to consider any validation for the new word.

# Save your program

# ----------------------------------------------


# new_word = input("Enter a new word: ")
# new_word = new_word.lower()
# word_list += [new_word]
# print(word_list)






# ----------------------------------------------
# Task 2.2 [4]

# Copy and paste your program from sub-task 2.1

# Extend your program to 
# - search the list to find words that have 5 or more letters
# - count and output the number of words that have five or more letters, with a suitable output message.

# Save your program 
# ----------------------------------------------


# new_word = input("Enter a new word: ")
# new_word = new_word.lower()
# word_list += [new_word]
# print(word_list)
# count = 0
# for i in range(len(word_list)):
#     if len(word_list[i]) >= 5:
#         count += 1 
# print("Number of words that have five or more letters: ",count)


# ----------------------------------------------
# Task 2.3 [3]

# Copy and paste your program from sub-task 2.2

# Extend your program to :
# - search the list to find words that begin and end with the same letter
# - count and output the number of words that begin and end with the same letter, with a suitable output message.

# Save your program for Task 2
# ----------------------------------------------

new_word = input("Enter a new word: ")
new_word = new_word.lower()
word_list += [new_word]
print(word_list)
count = 0
count1 = 0
for i in range(len(word_list)):
    if len(word_list[i]) >= 5:
        count += 1 
print("Number of words that have five or more letters: ",count)

for i in range(len(word_list)):
    if word_list[i][0] == word_list[i][-1]:
        count1 += 1
print("Number of words that begin and end with the same letter: ",count1)
               