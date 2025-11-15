with open("FiveLetterWords.txt","r") as f:
    contents = f.read().split(",")
    # print(contents)
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
