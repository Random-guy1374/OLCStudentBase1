def div_2(number):
      halved = int(number/2)
      return halved

def odd_or_even(number):
    if number%2 == 0:
        return "Even"
    elif number%2 == 1:
        return "Odd" 
# print(5**(1/2))
# print(5**(1/2)+1)
# print(1%1)

def prime(number):
    if number in [2,3]:
        return "Prime"
    else:
        if odd_or_even(number) == "Even" and number != 2:
            return "Not prime"
        else:
            count = 0
            half = int(div_2(number+1))
            for i in range(3,half):
                if number%i == 0:
                    count += 1
            if count == 0:
                return "Prime"
            else:
                return "Not prime"       


while True:
    num = float(input("Enter a whole number: "))
    if str(num//1) == str(num):
        break

print(f"{int(num)} is {prime(num)} number")


# for i2 in range(1,100):
#     if prime(i2) == 'Prime':
#         print(i2,prime(i2))

# def prime(number):
#     count = 0
#     num_root = int(number**(1/2)) + 1
#     for i in range(1,num_root):
#         if number%i == 0:
#             count += 1
#     if count == 1 and number != 1:
#         return "Prime"
#     else:
#         return "Not prime"

