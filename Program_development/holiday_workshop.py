############################################################
# TASK 5 - HOLIDAY WORKSHOP BOOKING SYSTEM
############################################################

# A school is organising several holiday workshops.
# The school requires a program to create and store for workshop bookings.

# Open a new JupyterLab notebook and save it as:
# TASK5_.ipynb

# For each sub-task, add a comment using the hash symbol '#'
# at the beginning of your code to indicate the sub-task that the program code belongs to.

# For example:
# # Task 5.1
# Program Code

# All code should have appropriate comments and all identifiers should be appropriately named. [4]

# The following workshops and fees are available:
# ROB - Robotics - $48.00 per student
# WEB - Web Design - $36.00 per student
# PYT - Python Programming - $42.00 per student

# You can assume that a parent's name contains at least
# three characters.

############################################################
# Task 5.1 [4]
############################################################

# Write a function valid_workshop_code() that:

# - takes workshop_code as a parameter;
# - checks that the workshop code contains exactly three characters;
# - checks that the workshop code is ROB, WEB or PYT;
# - accepts the workshop code regardless of letter case;
# - returns True if the workshop code is valid or False  otherwise.
# - Display the appropriate reason for non valid workshop codes.

# Save your program.
# Task 5.1 
#______________________________________________________________

# def valid_workshop_code(workshop_code):
#     code = True
#     if len(workshop_code) != 3 or workshop_code.upper() not in ["ROB","WEB","PYT"]:
#         code = False
#         print(f"Your code {workshop_code} is invalid.")
#     return code


# print(valid_workshop_code("pyt"))   
# print(valid_workshop_code("pytsdfsdf"))  







############################################################
# Task 5.2 [4]
############################################################

# Copy and paste your program from sub-task 5.1.

# Extend the program by writing a function
# calculate_booking_fee() that:

# - takes workshop_code (string) and number_of_students (integer) as parameters;
# - calculates the total fee using the appropriate fee per student;
# - deducts a discount of 10% if three or more students are included in the booking;
# - returns the total booking fee.

# You can assume that workshop_code and number_of_students are valid.

# Save your program.
# Task 5.2 
#______________________________________________________________

# def valid_workshop_code(workshop_code):
#     code = True
#     if len(workshop_code) != 3 or workshop_code.upper() not in ["ROB","WEB","PYT"]:
#         code = False
#         print(f"Your code {workshop_code} is invalid.")
#     return code

# def calculate_booking_fee(workshop_code, number_of_students):
#     total_cost = 0
#     if workshop_code.upper() == "ROB":
#         total_cost = number_of_students * 48
#     elif workshop_code.upper() == "WEB":
#         total_cost = number_of_students * 36
#     elif workshop_code.upper() == "PYT":
#         total_cost = number_of_students * 42
    
#     if number_of_students >= 3:
#         total_cost = round(total_cost * 0.9, 2)
#     return total_cost


# # print(valid_workshop_code("pyt"))   
# # print(valid_workshop_code("pytsdfsdf"))  
# print(calculate_booking_fee("pyt", 4))














############################################################
# Task 5.3 [2]
############################################################

# Copy and paste your program from sub-task 5.2.

# Extend the program by writing a function
# create_booking_reference() that:

# - takes parent_name and workshop_code as parameters;
# - generates a random six-digit booking number from 100000 to 999999 inclusive;
# - creates a booking reference containing:
#     - the first three characters of the parent's name in uppercase;
#     - the workshop code in uppercase;
#     - the six-digit booking number;
# - returns the booking reference.

# For example:
# Parent name: Siti
# Workshop code: pyt
# Random booking number: 583104
# Booking reference: SITPYT583104

# Save your program.
# Task 5.3
#______________________________________________________________
# import random 

# def valid_workshop_code(workshop_code):
#     code = True
#     if len(workshop_code) != 3 or workshop_code.upper() not in ["ROB","WEB","PYT"]:
#         code = False
#         print(f"Your code {workshop_code} is invalid.")
#     return code

# def calculate_booking_fee(workshop_code, number_of_students):
#     total_cost = 0
#     if workshop_code.upper() == "ROB":
#         total_cost = number_of_students * 48
#     elif workshop_code.upper() == "WEB":
#         total_cost = number_of_students * 36
#     elif workshop_code.upper() == "PYT":
#         total_cost = number_of_students * 42
    
#     if number_of_students >= 3:
#         total_cost = round(total_cost * 0.9, 2)
#     return total_cost

# def create_booking_reference(parent_name,workshop_code):
#     booking_ref = parent_name.upper()[:3] + workshop_code.upper() + str(random.randint(100000,999999))
#     return booking_ref

# # print(create_booking_reference("Siti","pyt"))
# # print(valid_workshop_code("pyt"))   
# # print(valid_workshop_code("pytsdfsdf"))  
# # print(calculate_booking_fee("pyt", 4))















############################################################
# Task 5.4 [11]
############################################################

# Copy and paste your program from sub-task 5.3.

# The school requires an interface for the workshop booking system.

# the program must:
# Part 1: 
# - ask for the parent's name;
# - ask for a workshop code; call valid_workshop_code() to check the workshop code;
#       - keep asking until a valid workshop code is entered; store the valid workshop code in uppercase;
# - ask for the number of students;
#       - Validate that the input is a valid number
#       - keep asking until a whole number from 1 to 5 inclusive is entered;
# - call calculate_booking_fee() to calculate the booking fee;
# - call create_booking_reference() to create a booking reference;
# - display the booking reference and booking fee clearly.
# - Save the booking reference into a list called booking_list.
# - After each booking, ask the user to enter C to continue or Q to stop.

# Part 2:
# - save all the booking references in booking_list to the file workshop_bookings.txt, with one booking reference on each line;
# - store the total fee for all bookings to two decimal places at the end of the workshop_bookings.txt file.
#   e.g. "Total Fee : $192.86"

# Suitable input and output messages must be used.
# Save your JupyterLab notebook for Task 5.

# Task 5.4 
#______________________________________________________________

import random 

def valid_workshop_code(workshop_code):
    code = True
    if len(workshop_code) != 3 or workshop_code.upper() not in ["ROB","WEB","PYT"]:
        code = False
        print(f"Your code {workshop_code} is invalid.")
    return code

def calculate_booking_fee(workshop_code, number_of_students):
    total_cost = 0
    if workshop_code.upper() == "ROB":
        total_cost = number_of_students * 48
    elif workshop_code.upper() == "WEB":
        total_cost = number_of_students * 36
    elif workshop_code.upper() == "PYT":
        total_cost = number_of_students * 42
    
    if number_of_students >= 3:
        total_cost = round(total_cost * 0.9, 2)
    return total_cost

def create_booking_reference(parent_name,workshop_code):
    booking_ref = parent_name.upper()[:3] + workshop_code.upper() + str(random.randint(100000,999999))
    return booking_ref

# Part 1: 
booking_feelist = []
booking_list = []
enter = "C"
while enter == "C":
    parent_name = input("Enter parent's name: ")
    while True:
        workshop_code = input("Enter workshop code: ")
        if valid_workshop_code(workshop_code) == True:
            break
    while True:
        num_student = input("Enter number of students: ")
        if num_student.isdigit():
            if int(num_student) >= 1 and int(num_student) <= 5:
                num_student = int(num_student)
                break
    booking_fee = calculate_booking_fee(workshop_code,num_student)
    booking_ref = create_booking_reference(parent_name,workshop_code)
    print(f"Your booking fee is ${booking_fee} and your booking reference is {booking_ref}")

    booking_list.append(booking_ref)
    booking_feelist.append(booking_fee)
    enter = input("Enter C to continue or Q to stop: ").upper()
    if enter == "Q":
        break

# Part 2:
with open("workshop_bookings.txt","w") as f:
    for i in range(len(booking_list)):
        msg = booking_list[i] + " Total Fee : " + str(booking_feelist[i]) + "\n"
        f.write(msg)

# print(create_booking_reference("Siti","pyt"))
# print(valid_workshop_code("pyt"))   
# print(valid_workshop_code("pytsdfsdf"))  
# print(calculate_booking_fee("pyt", 4))































#__________________________________________________________