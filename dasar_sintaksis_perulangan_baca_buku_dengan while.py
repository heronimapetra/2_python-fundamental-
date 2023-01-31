"""
Program perulangan membaca buku dengan While
"""

number_of_books = 10
print('Mother said, "read all of your books!"')

number_of_books_read = 0
print (f"number of books read {number_of_books_read}")

while number_of_books_read < number_of_books:
    number_of_books_read = number_of_books_read + 1
    print(f"book {number_of_books_read} has been read")

print(f"total number of books read {number_of_books_read} book")
