# Example:
# Input: "The quick brown fox jumps over the lazy dog."
# Output: "Valid sentence"

# Input: "the quick brown fox jumps over the lazy dog"
# Output: "Invalid sentence: does not start with a capital letter and does not end with a period"

# Input: "Hello world"
# Output: "Invalid sentence: does not end with a period"

sentence = input("Enter a sentence : ")
# words = sentence.split(" ")
# print(words)

while True:
    if sentence[0].isupper() == False:
        sentence = input("Invalid sentence need lowercase letter\nEnter a sentence :")
    elif (sentence[1:].islower() == False):
        sentence = input("Invalid sentence need uppercase letter\nEnter a sentence :")
    elif "." not in sentence:
        sentence = input("Invalid sentence need a period\nEnter a sentence :")
    elif " " not in sentence:
        sentence = input("Invalid sentence need a space\nEnter a sentence :")
    else:
        print("Valid sentence")
        break