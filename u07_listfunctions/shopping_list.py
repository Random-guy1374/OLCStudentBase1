shopping_list = []
while True:
    item = input("Input a shopping list (type quit to quit):").lower()
    if item == "quit":
        break
    if item in shopping_list:
        print("Item already added")
    if item not in shopping_list:
        print("Item added")
        shopping_list.append(item)
    
# print(shopping_list)