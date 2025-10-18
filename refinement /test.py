book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}
count = 0

book = input("Please enter the title of a book: ").lower()
book = book[0].upper() + book[1:]
if (book in book_authors) == True:
    print("The author of the",book,"is",book_authors[book])

add = input("Would you like to add a book? Y or N: ").lower()
if add == "y":
    book = input("Please enter the title of a book you would like to add: ").lower()
    book = book[0].upper() + book[1:]
    new_author = input("Enter the name of the author: ")
    book_authors[book] = new_author



amend = input("Would you like to change the author of a book? Y or N: ").lower()
if amend == "y":
    new_book = input("Please enter the title of a book you would like to change the author: ").lower()
    new_book = new_book[0].upper() + new_book[1:]
    while True:
        author_name = input("Enter the name of author that you would like to replace: ").lower()

        hasnum = False
        for c in author_name:
            if c.isdigit():
                hasnum = True
                break 

        # check if gotNum
        if hasnum:
            print("Author name cannot contain numbers.")
        else:
            book_authors[new_book] = author_name
            break


print("\n")
for char in book_authors:
    print(char,"by",book_authors[char])