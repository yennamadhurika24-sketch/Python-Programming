'''You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup).'''
def add(d1):
    key=input("Enter key=")
    value=input("enter value=")
    d1[key]=value
    print("Added successfully")
def remove(d1):
    key=input("Enter a key to remove")
    del d1[key]
    print("Removed successfully")
def search(d1):
    key=input("Enter a key to search=")
    print(d1[key])
def update(d1):
    key=input("Enter a key to update the value=")
    value=input("enter value=")
    d1[key]=value
    print(d1.items())
def display(d1):
    print(d1.items())
def keycount(d1):
    print("total number of books in the library=",len(d1))
def check(d1):
    value=input("Enter a value=")
    for k,v in d1.items():
        if v==value:
            print(k)
        

library = {}  # empty dictionary to store books
    
while True:
    print("\nLibrary Menu:")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. Update book")
    print("5. Display all books")
    print("6. Total books")
    print("7. Check by value")
    print("8. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == "1":
        add(library)
    elif choice == "2":
        remove(library)
    elif choice == "3":
        search(library)
    elif choice == "4":
        update(library)
    elif choice == "5":
        display(library)
    elif choice == "6":
        keycount(library)
    elif choice == "7":
        check(library)
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")


