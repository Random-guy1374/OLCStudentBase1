# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     else:
#         students = True

students = False
while students == False: #2. True to Flase
    comp = int(input("Enter the Computing test score ")) #4. add int
    math = int(input("Enter the Mathematics test score ")) #1 add "
    joint_score = comp + math #3. comp + comp to comp + math
    if comp == 100 and math == 100: #7. > to ==
        print("Student is awarded a gold award")
    elif(comp > 100 and math > 100) or joint_score >= 180: #5. add () #6. >= to =
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N': #6. More_scores to more_scores
        students = True
    else:
        students = False #7. True to False