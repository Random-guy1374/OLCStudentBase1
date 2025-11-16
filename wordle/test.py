import random
#1)
with open("FiveLetterWords.txt","r") as f:
    contents = f.read().split(",")

secret_word = contents[random.randint(1,len(contents))].upper()
print(secret_word)
user_word = input("(Guess1)Enter a 5-letter word: ")

list1 = []
list2 = []
for letter in secret_word:
    list1 += letter.upper()
for letter in user_word:
    list2 += letter.upper()
print(list1)
print(list2)

IstCount = [0, 0, 0, 0, 0]
for letter in range(len(list1)):
    if list1[letter] in list2:
        IstCount[letter] = "?"
    if list1[letter] == list2[letter]:
        IstCount[letter] = list1[letter]
    if list1[letter] not in list2:
        IstCount[letter] = "#"
print(IstCount)
