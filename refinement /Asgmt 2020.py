# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: ")
# pin = float(input("Please enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else:
#     print("Incorrect PIN for that locker")

while True:
    arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
    locker = int(input("Please enter the locker you would like to open: "))
    while True:
        if locker < 1 or locker > 10:
            locker = int(input("Number of the locker is not found.\nPlease enter the locker you would like to open: "))
        else:
            break

    pin = int(input("Please enter the PIN for the locker: "))
    while True:
        if len(str(pin)) != 4:
            pin = int(input("length of the PIN is out of range.\nPlease enter the PIN for the locker: "))
        else:
            break

    if pin == arraypins[locker-1]:
        print("The locker is open.")
        break
    else:
        print("Incorrect PIN for that locker")

