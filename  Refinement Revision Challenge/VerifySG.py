# ID = ""
# for i in range(2):
#     ID = input("Enter ID: ")
#     if ID[0] == "S":
#         print("Welcome home!")
#     else:
#         print("Welcome to Singapore!")

ID = ""
count = 0
num = int(input("How many IDs do you want to enter?: "))
for i in range(num):
    while True:
        ID = input("Enter ID: ")
        if len(ID) != 9:
            print("Invalid ID. Please enter a valid ID.")
        else:
            break
    if ID[0].upper() in ["S","T"]:
        print("Welcome home!")
        count += 1
    else:
        print("Welcome to Singapore!")
print("There are",count,"Singaporeans.")