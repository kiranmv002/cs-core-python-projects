# Attendance Analyzer System
# Day 4 Project - 2nd Year Academic Level

FILE_NAME = "attendance.txt"
TOTAL_CLASSES = 75  # You can change this if needed


def add_attendance():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    attended = int(input("Enter number of classes attended: "))

if attended < 0 or attended > TOTAL_CLASSES:
    print("Error: Invalid number of attended classes.")
    return

    percentage = (attended / TOTAL_CLASSES) * 100

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll_no},{name},{attended},{percentage:.2f}\n")

    print("Attendance record added successfully!")


def view_attendance():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nRoll No | Name | Attended | Percentage")
            print("-" * 50)
            for line in file:
                roll_no, name, attended, percentage = line.strip().split(",")
                print(f"{roll_no} | {name} | {attended} | {percentage}%")
    except FileNotFoundError:
        print("No attendance records found!")


def shortage_list():
    print("\nStudents with Attendance Shortage (<75%)")
    print("-" * 50)
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll_no, name, attended, percentage = line.strip().split(",")
                if float(percentage) < 75:
                    print(f"{roll_no} | {name} | {percentage}%")
                    found = True
        if not found:
            print("No students with shortage.")
    except FileNotFoundError:
        print("No attendance records found!")


def menu():
    while True:
        print("\n--- Attendance Analyzer System ---")
        print("1. Add Attendance Record")
        print("2. View All Attendance")
        print("3. Show Shortage List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            shortage_list()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
