# Student Record Sorting System
# Day 31 - DBMS Project

FILE_NAME = "student_records.txt"


def load_records():

    records = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:

            data = line.strip().split(",")

            records.append(data)

        file.close()

    except:
        print("File not found!")

    return records


def display(records):

    print("\nRoll No | Name | Marks")
    print("-" * 30)

    for record in records:

        print(record[0], "|", record[1], "|", record[2])


def sort_by_marks(records):

    records.sort(key=lambda x: int(x[2]), reverse=True)

    print("\nRecords Sorted by Marks")

    display(records)


def sort_by_name(records):

    records.sort(key=lambda x: x[1])

    print("\nRecords Sorted by Name")

    display(records)


# -------- MAIN --------

while True:

    print("\n--- Student Record Sorting ---")
    print("1. View Records")
    print("2. Sort by Marks")
    print("3. Sort by Name")
    print("4. Exit")

    choice = input("Enter choice: ")

    records = load_records()

    if choice == "1":

        display(records)

    elif choice == "2":

        sort_by_marks(records)

    elif choice == "3":

        sort_by_name(records)

    elif choice == "4":

        print("Exiting...")
        break

    else:
        print("Invalid choice!")
