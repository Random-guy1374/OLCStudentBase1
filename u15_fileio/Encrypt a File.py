letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# index = letters.find(letter)
with open("plaintext.txt", 'r') as f:
    word = f.read()
    the_word = ""
    for i in range(len(word)):
        letter = word[i]
        index = letters.find(letter)
        index = index + 3
        the_word = the_word + letters[index]
print(the_word)    
with open("encrypted.txt", 'w') as f: 
    f.write(the_word)
# with open("encrypted.txt", 'r') as f: 
#     print(f.read())