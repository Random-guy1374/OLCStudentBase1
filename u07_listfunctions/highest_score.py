Input = [87, 95, 76, 88, 95]
Output = 88
i = 0
#find highest score
for i in range(len(Input)):
    score1 = Input[i-1]
    score2 = Input[i]
    if score1 >= score2:
        highest = score1
    if score2 > score1:
        highest = score2
#remove highest score
while True:
    if highest in Input:
        Input.remove(highest)
    else:
        break
#finding highest score(2nd highest score)
for i in range(len(Input)):
    score1 = Input[i-1]
    score2 = Input[i]
    if score1 >= score2:
        final = score1
    if score2 > score1:
        final = score2
# print(Input)
print("The second highest score is",final)