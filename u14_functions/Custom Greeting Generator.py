import random

def generate_greet(the_input):
    greet = ""
    greet_list = [", Welcome to the event!", ", Glad to have you here!", ", It's great to see you!",", Thanks for joining us!"]
    # print(len(greet_list))
    name_list = the_input.split(" ")
    # print(name_list)
    for i in range(len(name_list)):
        random_greet = greet_list[random.randint(0,len(greet_list)-1)]
        name = name_list[i]
        greet += "\nHello " + name + random_greet + ""
    return greet

name = input("Enter a list of names (e.g. Alice Bob John): ")
result = generate_greet(name)
print(result)