# Employee Database Management System
# Day 37 - DBMS Project

FILE_NAME = "employees.txt"


def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    designation = input("Enter Designation: ")
    salary = input("Enter Salary: ")

    file = open(FILE_NAME, "a")
    file.write(emp_id + "," + name + "," + designation + "," + salary + "\n")
    file.close()

    print("Employee added successfully!")


def view_employees():

    try:
        file = open(FILE_NAME, "r")

        print("\nID | Name | Designation | Salary")
        print("-" * 45)

        for line in file:

            data = line.strip().split(",")

            print(data[0], "|", data[1], "|", data[2], "|", data[3])

        file.close()

    except:
        print("No employee records found!")


def search_employee():

    emp_id = input("Enter Employee ID: ")

    found = False

    try:
        file = open(FILE_NAME, "r")

        for line in file:

            data = line.strip().split(",")

            if data[0] == emp_id:

                print("\nEmployee Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Designation:", data[2])
                print("Salary:", data[3])

                found = True
                break

        file.close()

        if not found:
            print("Employee not found!")

    except:
        print("No employee records found!")


def delete_employee():

    emp_id = input("Enter Employee ID to delete: ")

    try:

        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()

        file = open(FILE_NAME, "w")

        deleted = False

        for line in records:

            if not line.startswith(emp_id + ","):
                file.write(line)
            else:
                deleted = True

        file.close()

        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")

    except:
        print("No employee records found!")


