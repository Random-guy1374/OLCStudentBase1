def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence

def check_list(word,word_string):
    if word in split_sentence(word_string):
        return "Yes"
    else:
        return "No"

def reverse_sentence(word_string):
    reverse_word = ""
    split_word_reverse = split_sentence(word_string)
    for char in split_word_reverse:
        reverse_word = char + " " + reverse_word 
    return reverse_word

string_word = input("Enter a string of word: ")
word = input("Enter a word to search: ")

print("String of a word split to a list:",split_sentence(string_word))
print("Reversed string of word:",reverse_sentence(string_word))

if check_list(word,string_word) == "Yes": # outputs whether the word input is found in the string of words. If word in string_word, 
    print(f"{word} is in {string_word}")
else:
    print(f"{word} is not in {string_word}")



