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



while True:
    user_answer = input("What do you have to do today. (Type 'nil' to stop): ")
    user_answer = user_answer.lower()
    if user_answer == "nil":
        break
    else:
        with open("task.txt","a") as f:
            f.write("\n")
            f.write(user_answer)
    with open("task.txt","r") as f:
        print(f.read())


