"""
Program perulangan membaca buku dengan While sampai paham
"""

book_count = 10
print('Mother said, "read all of your books!"')

read_count = 0

understood_count = 0
print (f"number of books read and understood {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"book {understood_count + 1} not yet understood")
    else:
        understood_count = understood_count + 1
        print(f"book {understood_count} have been read and understood")

print(f"total number of books read {understood_count} book")

if read_count == book_count:
    print("Mom, I have read and understood all of the books")
else:
    print(f"Mom, not all of books I can understand."
          f"Rini can only understand {understood_count} books")
