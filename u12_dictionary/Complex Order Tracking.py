orders = {
    "John": {"items": {"Apples": 3, "Bananas": 2}, "total": 15},
    "Mary": {"items": {"Oranges": 1, "Grapes": 4}, "total": 20},
    "Alice": {"items": {"Bananas": 5, "Pineapples": 2}, "total": 25},
}
orders["Mark"] = {"items": {"Apples": 2, "Oranges": 3}, "total": 18}
highest_bill = 0
for name, info in orders.items():
    if info["total"] >= highest_bill:
        highest_bill = info["total"]
        person = name
print(f"{person} has the highest total bill.")
