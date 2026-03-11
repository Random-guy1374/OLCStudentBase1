# number_people = 10
# minimum_height = 1.5
# for x in range(number_people):
#      name = input("Name of person: ")
#      height = float(input("Height of person: "))
#      if height >= minimum_height:
#            print("Person is tall enough")
#      else:
#            print("Person is not tall enough.")
minimum_height = 1.5
list_of_people = []
def check_age(age):
    if age >= 16:
        m1 = ("is old enough.")
        return True,m1
    else:
        m1 = ("is not old enough.")
        return False,m1

def check_height(h):
    if h >= 1.5:
        m2 = ("is tall enough")
        return True, m2
    else:
        m2 = (" is not tall enough")
        return False, m2

while True:
    name = input("Name of person (type q to quit): ")
    if name == 'q':
        break
    user_age = check_age(int(input("Age of person: ")))
    user_height = check_height(float(input("Height of person (cm): ")))
    # print(user_age[1],user_age[0])
    # print(user_height[1],user_height[0])
    if user_age[0] and user_height[0] == True:
        list_of_people += [name.capitalize()]
    if user_age[0] == user_height[0] :
        print(name.capitalize(),user_height[1],"and",user_age[1])
    # elif user_age[0] != user_height[0]:
    #     print(name.capitalize(),user_height[1],"but",user_age[1])
    elif user_age[0] != user_height[0] and user_age[0] == False:
        print(name.capitalize(),user_age[1])
    elif user_age[0] != user_height[0] and user_height[0] == False:
        print(name.capitalize(),user_height[1])
print("List of people who is qualified:",list_of_people)
    
    
