# Login & Authentication System
# Day 34 - DBMS Project

FILE_NAME = "users.txt"


def register():

    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open(FILE_NAME, "a")
    file.write(username + "," + password + "\n")
    file.close()

    print("User registered successfully!")


def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    try:

        file = open(FILE_NAME, "r")

        for line in file:

            data = line.strip().split(",")

            if data[0] == username and data[1] == password:

                print("Login Successful ✅")

                file.close()
                return

        file.close()

        print("Invalid Username or Password ❌")

    except:

        print("User database not found!")


while True:

    print("\n--- Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        register()

    elif choice == "2":

        login()

    elif choice == "3":

        print("Exiting...")
        break

    else:

        print("Invalid choice!")
