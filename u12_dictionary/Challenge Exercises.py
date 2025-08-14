students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
pass_dict = {}
fail_dict = {}
total = 0
for score in students.values():
    total = total + score
avg = total/len(students)
print(avg)
for name, grade in students.items():
    if grade >= avg:
        pass_dict[name] = grade

    else:
        fail_dict[name] = grade
print("Passed:",pass_dict.keys())
print("Failed:",fail_dict.keys())

