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

