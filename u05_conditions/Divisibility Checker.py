number = float(input("Enter : "))
if number % 2 == 0 and number % 3 == 0:
    print("Divisible by both.")
elif number % 2 != 0 and number % 3 == 0:
    print("Divisible by 3 only.")
elif number % 2 == 0 and number % 3 != 0:
    print("Divisible by 2 only.")
else:
    print("Not divisible by either.")
    
