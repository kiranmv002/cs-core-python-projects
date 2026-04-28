# Transaction & Rollback Simulation
# Day 22 - DBMS Project

FILE_NAME = "database.txt"


def read_data():
    try:
        file = open(FILE_NAME, "r")
        data = file.readlines()
        file.close()
        return data
    except:
        return []


def write_data(data):
    file = open(FILE_NAME, "w")
    file.writelines(data)
    file.close()


def transaction():

    print("\n--- Transaction Started ---")

    original_data = read_data()   # backup
    temp_data = original_data.copy()

    while True:

        print("\n1. Insert Record")
        print("2. Delete Record")
        print("3. View Temp Data")
        print("4. Commit")
        print("5. Rollback")

        choice = input("Enter choice: ")

        if choice == "1":
            record = input("Enter record (id,name,age): ")
            temp_data.append(record + "\n")
            print("Record added (not yet saved)")

        elif choice == "2":
            key = input("Enter ID to delete: ")
            new_data = []

            for line in temp_data:
                if not line.startswith(key + ","):
                    new_data.append(line)

            temp_data = new_data
            print("Record removed (not yet saved)")

        elif choice == "3":
            print("\n--- Temp Data ---")
            for line in temp_data:
                print(line.strip())

        elif choice == "4":
            write_data(temp_data)
            print("Transaction Committed ✅")
            break

        elif choice == "5":
            write_data(original_data)
            print("Transaction Rolled Back ❌")
            break

        else:
            print("Invalid choice!")


# -------- MAIN --------

while True:

    print("\n--- Transaction System ---")
    print("1. Start Transaction")
    print("2. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        transaction()
    elif ch == "2":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
