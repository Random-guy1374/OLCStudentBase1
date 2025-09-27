###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.


# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])

def greet_users(das_input):
    name_list = das_input
    greet_list = [", Welcome to the event!", ", Glad to have you here!",", Thanks for joining us!"]
    print(name_list[0],greet_list[0])
    print(name_list[1],greet_list[1])
    print(name_list[2],greet_list[2])
    return None

greet_users(["Alice", "Bob", "Charlie"])
print(greet_users)


#------------------------------------------------------------
# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

def calculator(the_input):
    final = 0
    number_list = the_input.split(",")
    f_num = int(number_list[0])
    s_num = int(number_list[1])
    symbol = input("Pick 1 (+) \nPick 2 (-) \nPick 3 (*)  \nPick 4 (/)\n: ")
    if symbol == "1":
        final = f_num + s_num
    elif symbol == "2": 
        final = f_num - s_num
    elif symbol == "3":
        final = f_num * s_num
    elif symbol == "4":
        final = f_num/s_num

    return final
num = input("Enter a number to calculate (e.g. 10,5): ")
result = calculator(num)
print("the result =",result)


#------------------------------------------------------------
# Exercise 9: Palindrome Checker
# Write a function that checks if a string is a palindrome.


# Test the function with different words.
# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))







#------------------------------------------------------------
# Exercise 10: Display Multiplication Table
# Write a function that takes a number and prints its multiplication table.

# Call the function with a number.
# multiplication_table(5)






#------------------------------------------------------------