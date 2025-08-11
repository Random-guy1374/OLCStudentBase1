scores = [90, 85, 92, 88, 76, 95, 89, 70]
highest = 0
second = 0
third = 0
for i in scores:
    if i > highest:
        highest = i
scores.remove(highest)

for i in scores:
    if i > second:
        second = i
scores.remove(second)        
for i in scores:
    if i > third:
        third = i
scores.remove(third)

# print(highest)
print("Second place got :",second)
print("Third place got :",third)


