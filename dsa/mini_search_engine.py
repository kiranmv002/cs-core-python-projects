# Mini Search Engine
# Day 30 - Data Structures Project

FILE_NAME = "documents.txt"


def search_word(keyword):

    try:
        file = open(FILE_NAME, "r")

        lines = file.readlines()

        found = False

        print("\nSearch Results:\n")

        for line_no, line in enumerate(lines, start=1):

            if keyword.lower() in line.lower():

                print(f"Line {line_no}: {line.strip()}")

                found = True

        file.close()

        if not found:
            print("No matching results found.")

    except:
        print("File not found!")


# -------- MAIN --------

while True:

    print("\n--- Mini Search Engine ---")
    print("1. Search Keyword")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        keyword = input("Enter keyword to search: ")

        search_word(keyword)

    elif choice == "2":

        print("Exiting...")
        break

    else:
        print("Invalid choice!")
