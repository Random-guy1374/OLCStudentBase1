import random

def generate_username(the_input):
    name_list = the_input.split(' ')
    # print(name_list)
    first_name = name_list[0]
    last_name = name_list[1]
    animal = ["Tiger", "Lion", "Bear", "Wolf", "Eagle"]
    random_number = random.randint(10,99)
    random_animal = animal[random.randint(0,len(animal))]
    username = first_name + last_name + random_animal + str(random_number)
    return username

name = input("First name and Last name (E.g. John Lake): ")
result = generate_username(name)
print("Your username is",result)