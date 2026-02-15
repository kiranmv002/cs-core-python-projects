# Mini File-Based Database System
# Day 9 - DBMS Project

FILE_NAME = "database.txt"


def insert_record():
    record_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{record_id},{name},{age}\n")

    print("Record inserted successfully!")


def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nID | Name | Age")
            print("-" * 25)
            for line in file:
                record_id, name, age = line.strip().split(",")
                print(f"{record_id} | {name} | {age}")
    except FileNotFoundError:
        print("No records found!")


def search_record():
    search_id = input("Enter ID to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                record_id, name, age = line.strip().split(",")
                if record_id == search_id:
                    print("\nRecord Found:")
                    print(f"ID: {record_id}")
                    print(f"Name: {name}")
                    print(f"Age: {age}")
                    found = True
                    break

        if not found:
            print("Record not found!")
    except FileNotFoundError:
        print("No records found!")


def delete_record():
    delete_id = input("Enter ID to delete: ")
    records = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                record_id, name, age = line.strip().split(",")
                if record_id != delete_id:
                    records.append(line)
                else:
                    found = True

        with open(FILE_NAME, "w") as file:
            for record in records:
                file.write(record)

        if found:
            print("Record deleted successfully!")
        else:
            print("Record not found!")

    except FileNotFoundError:
        print("No records found!")


def menu():
    while True:
        print("\n--- Mini Database System ---")
        print("1. Insert Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
