# Ashmin Jayson 14 S4 DS
# ExperimentNo : 10 Program to implement dictionary in python
# Date : 17/05/2022


def add_book(books, title, stock):
    if title in books :
        print("Book already exists")
        return 
    books[title] = stock


def update_shelf(books): 
    print("1.Increase stock : ")
    print("2.Decrease stock : ")
    ch = int(input())

    title = input("Enter the title of book to update stock of : ")
    if ch == 1 :
        print("Enter the amount to increase by : ")
        inc = int(input())
        books[title] = books[title] + inc
    if ch == 2 : 
        print("Enter the amount to decrease by : ")
        dec = int(input())
        books[title] = books[title] - dec


def remove_book(books, title):
    test = books.pop(title, "Book not present")
    if test == "Book not present":
        print("Book not present")
 
def display(books):
    print("Books  Stock")
    for i in books: 
        print(i, end = "   ")
        print(books[i])

books = {}
i = 1
while i == 1 : 
    print("MENU")
    print("1.Add Book")
    print("2.Delete Book")
    print("3.Update Stock")
    print("4.Display Books")
    x = int(input())

    if x == 1 : 
        print("Enter the title of the book to add : ")
        title = input()
        print("Enter the corresponding stock : " )
        stock = int(input())
        add_book(books, title, stock)

    if x == 2 : 
        print("Enter the title of the book to remove : ")
        title = input()
        remove_book(books, title)

    if x == 3 : 
        update_shelf(books)
    if x == 4 : 
        display(books)
    
    print("Return to menu : 1 / 0 " )
    i = int(input())
    
    
    
    
# Output : 

# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 1
# Enter the title of the book to add : 
# TalesofKris
# Enter the corresponding stock : 
# 21
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 1
# Enter the title of the book to add : 
# Chroma
# Enter the corresponding stock : 
# 2
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 3
# 1.Increase stock : 
# 2.Decrease stock : 
# 1
# Enter the title of book to update stock of : Chroma
# Enter the amount to increase by : 
# 2
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 4
# Books  Stock
# TalesofKris   21
# Chroma   4
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 2
# Enter the title of the book to remove : 
# TalesofKris
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 4
# Books  Stock
# Chroma   4
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 2
# Enter the title of the book to remove : 
# Chroma
# Return to menu : 1 / 0 
# 1
# MENU
# 1.Add Book
# 2.Delete Book
# 3.Update Stock
# 4.Display Books
# 4
# Books  Stock
# Return to menu : 1 / 0 
# 0


