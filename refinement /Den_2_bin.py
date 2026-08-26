# NEW_BASE == 3
# num = Input("Enter a non-negative integer: "
# num = float(num)
# result = ""
# q = num
# r = q % NEW_BASE
# result = str(r) + result
# q = q // NEW_BASE
# while q > 0
#     r = q % NEW_BASE
#     result = result + str(r)
#     q = q / NEW_BASE
#     print(result, "in Decimal is", num, "in Binary.")




# Task 3
# The following program should read a denary non-negative integer from the user. 
# The program will then convert the denary integer to its 
#    binary value and print it to the screen. 
# The “division by 2” method is employed to carry out the conversion. 
# There are several syntax errors and logical errors in the program.

NEW_BASE = 2 #1) change == to = 6) change 3 to 2
num = input("Enter a non-negative integer: ") #2) change Input to input 3) add )
num = int(num) #5) change float() to int()
result = ""
q = num
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE
while q > 0: #4) add :
    r = q % NEW_BASE
    result = str(r) + result #11) change result + str(r) to str(r) + result
    q = q // NEW_BASE #7) change / to //
print(num, "in Decimal is", result, "in Binary.") #8) change result to num #9) change num to result #10) untab

# Open the file D2B.py
# Save the file as MYD2B___
# 
# Identify and correct the errors in the program so that it 
# works correctly according to the description above. Save your program.
#  [10] 