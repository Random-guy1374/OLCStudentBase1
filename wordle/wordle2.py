#1)
with open("FiveLetterWords.txt","r") as f:
    contents = f.read().split(",")

#2)
WORD = "sunny"
vowels = ['a','e','i','o','u']
IstCount = [0, 0, 0, 0, 0]
# letters = []
# for letter in WORD:
#     letters += letter
# print(letters)
for letter in range(len(WORD)):
    if WORD[letter] in vowels:
        IstCount[letter] = letter
print(IstCount)

#3)
Alphablet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
for i in Alphablet:
    IstCount = [0, 0, 0, 0, 0]
    for word in contents: 
        for a in range(len(word)):
            if word[a] == i:
                IstCount[a] += 1
    print(f"{i} is {IstCount}")

# # A
# IstCount = [0, 0, 0, 0, 0]
# for word in contents: 
#     for a in range(len(word)):
#         if word[a] == "a":
#             IstCount[a] += 1
# print(f"a is {IstCount}")

# # E
# IstCount = [0, 0, 0, 0, 0]
# for word in contents: 
#     for e in range(len(word)):
#         if word[e] == "e":
#             IstCount[e] += 1
# print(f"e is {IstCount}")

# # I 
# IstCount = [0, 0, 0, 0, 0]
# for word in contents: 
#     for i in range(len(word)):
#         if word[i] == "i":
#             IstCount[i] += 1
# print(f"i is {IstCount}")

# # O 
# IstCount = [0, 0, 0, 0, 0]
# for word in contents: 
#     for o in range(len(word)):
#         if word[o] == "o":
#             IstCount[o] += 1
# print(f"o is {IstCount}")

# # U
# IstCount = [0, 0, 0, 0, 0]
# for word in contents: 
#     for j in range(len(word)):
#         if word[j] == "u":
#             IstCount[j] += 1
# print(f"u is {IstCount}")