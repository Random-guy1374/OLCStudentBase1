import random
# with open("file.txt","w") as f:
#     f.write("Cheese\n") 

# with open("file.txt","r") as f:
#     print(f.read())

# new_input = input("Enter a word:")
# with open("file.txt","a") as f:
#     f.write("\n")
#     f.write(new_input)

# with open("file.txt","r") as f:
#     print(f.read())
#     result = f.read()

#     count_a = 0

#     for c in result:
#         if c.lower() == "a":
#             count_a += 1
#         # elif c.lower() == "r":
#         #     count_r += 1
#     print("There are",count_a,"A in the file")

# with open('file.txt','r') as f:
#     daylist = f.readlines()

#     for day in daylist:
#         print(day)

# random_day = random.choice(daylist)
# print("Random day:",random_day)

# planets_list = ["mercury\n","venus\n","earth\n","mars\n","jupiter\n","saturn\n","uranus\n"]
# with open("planets.txt","w") as f:
#     f.writelines(planets_list)



# while True:
#     user_answer = input("What do you have to do today. (Type 'nil' to stop): ")
#     user_answer = user_answer.lower()
#     if user_answer == "nil":
#         break
#     else:
#         with open("task.txt","a") as f:
#             f.write("\n")
#             f.write(user_answer)
#     with open("task.txt","r") as f:
#         print(f.read())





# Exercise 7: Read and Print Each Line
# Open "example.txt" and print each line individually.
# Ensure "example.txt" exists with some content.
print("Exercise 7: Read and Print Each Line")
with open("example.txt",'r') as f:
    content = f.readlines()
    for word in content:
        print(word)




#------------------------------------------------------------
# Exercise 8: Write User Input to File
# Ask the user for three lines of input and save them to "user_input.txt".


# print("\nExercise 8: Write User Input to File")
# with open("user_input",'a') as f:
#     for i in range(3):
#         user_input = input("Enter : ")
#         f.write(user_input)
#         f.write("\n")
# with open("user_input",'r') as f:
#     content2 = f.readlines()
# print(content2)






#------------------------------------------------------------
# Exercise 9: Count Words in File
# Count the total number of words in "example.txt".
print("\nExercise 9: Count Words in File")





#------------------------------------------------------------
# Exercise 10: Append a Line to File
# Add "This is a new line added during class." to "example.txt".






#------------------------------------------------------------
# Exercise 11: Create a Simple To-Do List
# Let the user add three to-do tasks to "todo.txt".






#------------------------------------------------------------
# Exercise 12: Combine Two Files (Simplified)
# Open "file1.txt" and "file2.txt" individually and write their contents to "combined.txt".