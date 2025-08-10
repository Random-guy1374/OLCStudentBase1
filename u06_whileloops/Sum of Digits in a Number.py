number = input("Enter a number : ")
total = 0
i = 0
length = float(len(number))
while True:
    if i != length:
        digit = number[i]
        total = total + float(digit)
        i += 1
    if i == length:
        break
print(total)