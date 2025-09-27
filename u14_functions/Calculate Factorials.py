def factorise(number):
    num = 1
    final = 1
    while num <= (number):
        final = final*num
        # print(final)
        num += 1

    return final

number = int(input("Enter a number to factorise: "))
result = factorise(number)
print("Factorial of",number,"is",result)