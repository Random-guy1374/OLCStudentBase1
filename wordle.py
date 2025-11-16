#1)
with open("FiveLetterWords.txt","r") as f:
    contents = f.read().split(",")
    # print(contents)

#2?
empty = []
vowels = ["a","e","i","o","u"]
letters = []
for word in contents:
    vowel = 0 # for every word, reset vowel count
    for v in vowels:
        if v in word:
            vowel += 1 
    if vowel >= 4 :
        empty += [word]
print(empty)

#3)
vowel1 = [] 
vowel2 = []
vowel3 = []
vowel4 = []
vowel5 = []
letters = []
for word in contents:
    vowel = 0 # for every word, reset vowel count
    for v in vowels:
        if v in word:
            vowel += 1 
    if vowel == 1:
        vowel1 += [word]
    if vowel == 2:
        vowel2 += [word]
    if vowel == 3:
        vowel3 += [word]
    if vowel == 4:
        vowel4 += [word]
    if vowel == 5:
        vowel5 += [word]
#4)
# print("words with 1 vowel:",vowel1)
# print("\n")
# print("words with 2 vowel:",vowel2)
# print("\n")
# print("words with 3 vowel:",vowel3)
# print("\n")
print("words with 4 vowel:",vowel4)
print("\n")
print("words with 5 vowel:",vowel5)

# user_word = input("Enter a 5 letters word: ")
# while True:
#     if len(user_word) != 5:
#         user_word = input("Enter a 5 letters word: ")

# loop through all the words in the list

# count the number of unique vowels by doing the below
    # loop through all possible vowels a, e, i, o, u
        # check if this current vowel e.g. a is in the word
            # vowelcount += 1

# if the number of vowels is 4 
    # add to fourletterwords list
