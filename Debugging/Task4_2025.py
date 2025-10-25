# group_1 = []
# group_2 = []
# group_3 = []
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_name = first_name[1]
#     age = input("Please enter the child's age: ")
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter >= "M" or age > 10:
#         group_2 = group_2 + [first_name]
#     elif age < 10:
#         group_3 = group_3 + [first_name]
#         count += 1
#     more = input("Do you have another child to enter, Y or N?: ")
#     if more == "Y":
#         flag = False

# print("You have entered the names of", flag, "children")
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)

group_1 = []
group_2 = []
group_3 = []
flag = True
count = 0 #7 add count = 0
while flag:
    first_name = input("Please enter the child's name: ").upper()
    first_letter = first_name[0] #1 first_name  to first_letter #9 change [1] to [0]
    age = int(input("Please enter the child's age: ")) #10 add int()
    if (first_letter >= "A" and first_letter <= "M") and age > 10: #3 add ()
        group_1 = group_1 + [first_name]
    elif first_letter >= "M" and age > 10: #5 change or to and
        group_2 = group_2 + [first_name]
    elif age <= 10: #6 change < to <=
        group_3 = group_3 + [first_name]
    count += 1 #8 untab count += 1
    more = input("Do you have another child to enter, Y or N?: ").upper() #2 add .upper()
    if more == "N":#11 change Y to N
        flag = False

print("You have entered the names of", count, "children") #4 change flag to count
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)