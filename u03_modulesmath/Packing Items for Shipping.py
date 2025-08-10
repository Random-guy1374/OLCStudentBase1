item = float(input("Items : "))
cap = float(input("Capacity : "))

container = item//cap
remain = item%cap

print("\nFull container :",container)
print("Leftover :",remain)
