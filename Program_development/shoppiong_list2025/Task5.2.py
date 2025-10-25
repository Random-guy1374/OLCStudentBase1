#task 5.2
def discount(cost):
    cost_with_tax = cost*1.09
    if cost > 50 and cost < 100:
        cost_with_tax *= 0.85
    elif cost >= 100:
        cost_with_tax *= 0.9

    return cost_with_tax
cost = float(input("Enter the price of the product: "))
print(discount(cost))
