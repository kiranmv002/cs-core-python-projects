
# Student Result Processing System
# Academic Project for 2nd Year CS Student

FILE_NAME = "student_results.txt"


def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


def add_student_result():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for i in range(subjects):
        mark = int(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / subjects
    grade = calculate_grade(percentage)

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll_no},{name},{total},{percentage:.2f},{grade}\n")

    print("Student result added successfully!")


def view_results():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nRoll No | Name | Total | Percentage | Grade")
            print("-" * 45)
            for line in file:
                roll_no, name, total, percentage, grade = line.strip().split(",")
                print(f"{roll_no} | {name} | {total} | {percentage}% | {grade}")
    except FileNotFoundError:
        print("No results found!")


def menu():
    while True:
        print("\n--- Student Result Processing System ---")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student_result()
        elif choice == "2":
            view_results()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
