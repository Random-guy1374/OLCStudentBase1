# num_students = 10
# for x in range(num_students):
#     colour = input(“What is the student’s favourite colour?”)

colour_list = []
dict_of_colours = {}
highest  = 0
num_students = 10
while True:
    colour = input("What is the student's favourite colour? (Type q to quit): ")
    s_colour = colour.lower()
    if colour == 'q':
        break
    if s_colour not in colour_list:
        colour_list += [s_colour]
        dict_of_colours[s_colour] = 1
        for s_colour in dict_of_colours:
            if dict_of_colours[s_colour] > highest:
                highest = dict_of_colours[s_colour]
                favorite_colour = s_colour
                # print(highest)
                # print(colour)
    else:
        dict_of_colours[s_colour] += 1
        for s_colour in dict_of_colours:
            if dict_of_colours[s_colour] > highest:
                highest = dict_of_colours[s_colour]
                favorite_colour = s_colour
                # print(highest)
                # print(colour)
    
print("Most favourite colour is",favorite_colour,"with a total of",highest,"students like this colour.")