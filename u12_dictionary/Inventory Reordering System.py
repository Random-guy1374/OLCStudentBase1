inventory = {"Apples": 50, "Bananas": 10, "Oranges": 20, "Grapes": 5, "Pineapples": 40}
print("Item with stock below 15")
total = 0
for item, price in inventory.items():
    if price < 15:
        print(item)
    total = total + price
for product, cost in inventory.items():
    percent = (cost/total)*100 
    print(f"{product} is {percent}% of our stock")

    

