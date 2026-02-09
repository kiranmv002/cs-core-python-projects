# Library Management System (File Based)
# 2nd Year Academic Project

FILE_NAME = "books.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")

    print("Book added successfully!")


def view_books():
    try:
        with open(FILE_NAME, "r") as f:
            print("\nID\tTitle\tAuthor\tStatus")
            for line in f:
                book_id, title, author, status = line.strip().split(",")
                print(f"{book_id}\t{title}\t{author}\t{status}")
    except FileNotFoundError:
        print("No books found!")


def issue_book():
    book_id = input("Enter Book ID to issue: ")
    books = []
    issued = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == book_id and data[3] == "Available":
                    data[3] = "Issued"
                    issued = True
                books.append(",".join(data))

        with open(FILE_NAME, "w") as f:
            for book in books:
                f.write(book + "\n")

        if issued:
            print("Book issued successfully!")
        else:
            print("Book not available or invalid ID!")

    except FileNotFoundError:
        print("No books found!")


def return_book():
    book_id = input("Enter Book ID to return: ")
    books = []
    returned = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == book_id and data[3] == "Issued":
                    data[3] = "Available"
                    returned = True
                books.append(",".join(data))

        with open(FILE_NAME, "w") as f:
            for book in books:
                f.write(book + "\n")

        if returned:
            print("Book returned successfully!")
        else:
            print("Invalid Book ID!")

    except FileNotFoundError:
        print("No books found!")


def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
