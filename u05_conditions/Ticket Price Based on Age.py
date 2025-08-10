child = 10
adult = 20
senoir = 15
age = float(input("Enter your age: "))
if age < 12:
    print(f"Your ticket price is ${child}.")
if 12 <= age < 60:
    print(f"Your ticket price is ${adult}.")
if age >= 60:
    print(f"Your ticket price is ${senoir}.")