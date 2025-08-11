list_a = ["apple", "banana", "cherry", "date", "elderberry"]
list_b = ["banana", "cherry", "date", "fig", "grape"]
list_c = []
for i in list_a:
    if i in list_b:
        list_c.append(i)
print("Similarity :",list_c)