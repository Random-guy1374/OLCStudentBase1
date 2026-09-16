students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
pass_dict = {}
fail_dict = {}

total = sum(students.values())
pass_score = 80
avg = float(total/len(students))
below_avg = []

for name, score in students.items():
    if float(score) < avg:
        below_avg.append(name)
    if score < 80:
        fail_dict[name] = score
    elif score >= 80:
        pass_dict[name] = score
print(f"students who scored below average of {avg}: {below_avg}")