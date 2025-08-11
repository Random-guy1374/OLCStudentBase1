number = float(input("Enter a number : "))
final = number
while  True:
    print(final)
    if final == 1:
        break
    elif final % 2 == 0:
        final = final/2
    elif final % 2 == 1:
        final = (final*3)
        final += 1
