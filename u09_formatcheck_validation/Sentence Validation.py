sentence = input("Enter a sentence : ")
while True:
    if sentence.upper == sentence:
        sentence = input("Invalid sentence need lowercase letter\nEnter a sentence :")
    if sentence.lower == sentence:
        sentence = input("Invalid sentence need uppercase letter\nEnter a sentence :")
    if "." not in sentence:
        sentence = input("Invalid sentence need a period\nEnter a sentence :")
    if " " not in sentence:
        sentence = input("Invalid sentence need a space\nEnter a sentence :")
    else:
        print("Valid sentence")
        break