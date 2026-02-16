# Mini File-Based Database System
# Day 10 - Added Update Record Feature

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


def update_record():
    update_id = input("Enter ID to update: ")
    records = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                record_id, name, age = line.strip().split(",")

                if record_id == update_id:
                    print("Record Found. Enter new details:")
                    new_name = input("Enter new name: ")
                    new_age = input("Enter new age: ")
                    records.append(f"{record_id},{new_name},{new_age}\n")
                    found = True
                else:
                    records.append(line)

        with open(FILE_NAME, "w") as file:
            for record in records:
                file.write(record)

        if found:
            print("Record updated successfully!")
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
        print("5. Update Record")
        print("6. Exit")

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
            update_record()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
