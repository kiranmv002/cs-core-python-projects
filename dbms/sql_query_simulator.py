# Simple SQL Query Simulator
# Day 11 - DBMS Project

FILE_NAME = "database.txt"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            data = []
            for line in file:
                record_id, name, age = line.strip().split(",")
                data.append({"id": record_id, "name": name, "age": age})
            return data
    except FileNotFoundError:
        print("Database file not found!")
        return []


def select_all(data):
    print("\nID | Name | Age")
    print("-" * 25)
    for record in data:
        print(f"{record['id']} | {record['name']} | {record['age']}")


def select_where(data):
    search_id = input("Enter ID to search: ")
    found = False

    for record in data:
        if record["id"] == search_id:
            print("\nRecord Found:")
            print(f"{record['id']} | {record['name']} | {record['age']}")
            found = True

    if not found:
        print("Record not found!")


def delete_where(data):
    delete_id = input("Enter ID to delete: ")
    new_data = []
    found = False

    for record in data:
        if record["id"] != delete_id:
            new_data.append(record)
        else:
            found = True

    if found:
        with open(FILE_NAME, "w") as file:
            for record in new_data:
                file.write(f"{record['id']},{record['name']},{record['age']}\n")
        print("Record deleted successfully!")
    else:
        print("Record not found!")


def menu():
    while True:
        print("\n--- SQL Query Simulator ---")
        print("1. SELECT *")
        print("2. SELECT WHERE id")
        print("3. DELETE WHERE id")
        print("4. Exit")

        choice = input("Enter choice: ")

        data = load_data()

        if choice == "1":
            select_all(data)
        elif choice == "2":
            select_where(data)
        elif choice == "3":
            delete_where(data)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
