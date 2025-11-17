import random
#1)
with open("FiveLetterWords.txt","r") as f:
    contents = f.read().split(",")

#2) 
secret_word = contents[random.randint(1,len(contents))].upper()
print(secret_word)

#3)
user_word = input("(Guess1)Enter a 5-letter word: ")
list1 = []
list2 = []
for letter in secret_word:
    list1 += letter.upper()
for letter in user_word:
    list2 += letter.upper()

IstCount = [0, 0, 0, 0, 0]
for letter in range(len(list1)):
    if list1[letter] in list2:
        IstCount[letter] = "?"
    if list1[letter] == list2[letter]:
        IstCount[letter] = list1[letter]
    if list1[letter] not in list2:
        IstCount[letter] = "#"
                
print(IstCount)     


def check(user_word):
    while True:
        if user_word.isalpha() != True:
            user_word = input("Invalid word must contain only letters\nEnter a 5-letter word: ")
        if len(user_word) != 5:
            user_word = input("Invalid word must cantain only 5 letters\nEnter a 5-letter word: ")
        if user_word.lower() not in contents:
            user_word = input("Invalid must be a real word\nEnter a 5-letter word: ")
        else:
            break
check(user_word)
    
#4)
guess = 2
while True:
    if guess == 7:
        print("Sorry you run out of guesses the word is",secret_word)
        break
    if user_word.upper() != secret_word.upper():
        user_word = input(f"(Guess{guess})Enter a 5-letter word: ")
        check(user_word)
        list1 = []
        list2 = []
        for letter in secret_word:
            list1 += letter.upper()
        for letter in user_word:
            list2 += letter.upper()

        IstCount = [0, 0, 0, 0, 0]
        position = [1, 2, 3, 4, 5]
        for letter in range(len(list2)):
            if list2[letter] in list1:
                IstCount[letter] = "?"
            if list2[letter] == list1[letter]:
                IstCount[letter] = list1[letter]
            if list2[letter] not in list1:
                IstCount[letter] = "#"
                    
        print(IstCount)
        guess += 1
    if user_word.upper() == secret_word.upper():
        print("congratulation you WIN!! you guess the right word")
        break
     




