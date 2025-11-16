#1)
with open("FiveLetterWords.txt","r") as f:
    contents = f.read().split(",")

#2)
Alphablet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
Alpha_num = {}
for i in Alphablet:
    count = 0
    for word in contents: 
        if i in word:
            count += 1
    Alpha_num[i] = count
    print(f"{i} is {count}")

#3)
# print(Alpha_num)
leaderboard = {}
reversed_leaderboard = {}
Alpha_num2 = Alpha_num
Alpha_num3 = Alpha_num

while Alpha_num2:
    top_letter = ""
    top_freq = 0
    least_freq = 100000
    least_letter = ""
    for letter in Alpha_num2:
        if Alpha_num2[letter] > top_freq:
            top_letter = letter
            top_freq = Alpha_num2[letter]
    leaderboard[top_letter] = top_freq

    for letter in Alpha_num3:
        if Alpha_num2[letter] < least_freq:
            least_letter = letter
            least_freq = Alpha_num2[letter]
    reversed_leaderboard[least_letter] = least_freq

    del Alpha_num2[top_letter]
    del Alpha_num2[least_letter]

#4)
print("reversed_leaderboard",leaderboard)
print("reversed_leaderboard",reversed_leaderboard)

position = 1
print("Top 10")
for lett,num in leaderboard.items():
    if position >= 11:
        break
    print(f"{position}) {lett} : {num}")
    position += 1

#5)
print("Top last 10")
position = 1
for lett,num in reversed_leaderboard.items():
    if position >= 11:
        break
    print(f"{position}) {lett} : {num}")
    position += 1

# print(leaderboard)

