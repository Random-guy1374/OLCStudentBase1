
books = {
    "1984": {"status": "Available", "copies": 5, "borrowed": 3},
    "Brave New World": {"status": "Checked Out", "copies": 0, "borrowed": 5},
    "Fahrenheit 451": {"status": "Available", "copies": 2, "borrowed": 1},
}
most_borrowed = 0
book_title = ""
for title, info in books.items():
   if info["borrowed"] > most_borrowed:
      most_borrowed = info["borrowed"]
      book_title = title

print(f"{title} has the most borrwed which is {most_borrowed}")
books["Berserk"] = {"status": "Available", "copies": 3, "borrowed": 19}

for title, info in books.items():
   if info["borrowed"] > most_borrowed:
      most_borrowed = info["borrowed"]
      book_title = title

print(f"{title} has the most borrwed which is {most_borrowed}")