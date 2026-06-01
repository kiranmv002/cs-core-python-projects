# Hospital Management System

FILE_NAME = "patients.txt"


def add_patient():

    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")

    file = open(FILE_NAME, "a")
    file.write(pid + "," + name + "," + age + "," + disease + "\n")
    file.close()

    print("Patient added successfully!")


def view_patients():

    try:
        file = open(FILE_NAME, "r")

        print("\nID | Name | Age | Disease")
        print("-" * 40)

        for line in file:
            data = line.strip().split(",")
            print(data[0], "|", data[1], "|", data[2], "|", data[3])

        file.close()

    except:
        print("No records found!")


def search_patient():

    pid = input("Enter Patient ID: ")

    found = False

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        if data[0] == pid:

            print("\nPatient Found")
            print("ID:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Disease:", data[3])

            found = True
            break

    file.close()

    if not found:
        print("Patient not found!")
