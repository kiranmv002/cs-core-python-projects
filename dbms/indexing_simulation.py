# DBMS Indexing Simulation
# Day 20 Project

FILE_NAME = "database.txt"


def build_index():
    index = {}

    try:
        file = open(FILE_NAME, "r")

        position = 0

        for line in file:
            data = line.strip().split(",")

            record_id = data[0]

            index[record_id] = position

            position += 1

        file.close()

        return index

    except:
        print("Database file not found!")
        return {}


def search_record(index):
    key = input("Enter ID to search: ")

    if key in index:
        file = open(FILE_NAME, "r")

        lines = file.readlines()

        record = lines[index[key]]

        print("\nRecord Found:")
        print(record)

        file.close()

    else:
        print("Record not found!")


def main():

    index = build_index()

    while True:

        print("\n--- Indexing Simulation ---")
        print("1. Search Record using Index")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            search_record(index)

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


main()
