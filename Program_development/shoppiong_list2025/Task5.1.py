#task 5.1
def total_cost(cost):
    cost_with_tax = cost*1.09
    return cost_with_tax

# cost = float(input("Enter the price of the product: "))
# total = total_cost(cost)
# print(total)

#task 5.2
def discount(cost):
    cost_after_dis = total_cost(cost)
    if cost > 50 and cost < 100:
        cost_after_dis *= 0.95
        return cost_after_dis
    elif cost >= 100:
        cost_after_dis *= 0.9
        return cost_after_dis
    else:
        return cost_after_dis

# paid = discount(cost)
# print(paid)

# import math
# math.floor(40.87) # 40

# 40.87 // 1
#task5.3
def reward_points(discount_total):
    points = (discount_total//1)/3
    return points

#task 5.4
def voucher(price,name):
    name = name.upper()
    if price > 25 and price < 50:
        fix_code = "05PERCENT"
        voucher = name[:3] + fix_code
        return voucher
    elif price >= 50:
        fix_code = "10PERCENT"
        voucher = name[:3] + fix_code
        return voucher
    else:
        message = "You need to spend over $25 for a voucher code."
        return message
    
#task5.5

name = input("Enter your name: ")
cost = float(input("Enter the price of the product: "))

total = total_cost(cost)
discount_total = discount(cost)
points = reward_points(discount_total)
code = voucher(discount_total,name)


print("Receipt")
print("The total cost:",round(total,2))
print("The total cost after discount:",round(discount_total,2))
print("Points recieved:",round(points,2))
print(code)
