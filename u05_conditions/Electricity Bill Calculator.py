unit = float(input("Enter : "))

if unit <= 100:
    bill = unit * 0.5
elif unit <= 200:
    bill = (100 * 0.5) + ((unit - 100) * 0.75)
elif unit > 200:
    bill = (100 * 0.5) + (100 * 0.75) + ((unit - 200) * 1)
print("Total bill is $",bill)