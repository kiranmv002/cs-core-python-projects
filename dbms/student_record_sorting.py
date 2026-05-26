# Student Record Sorting System
# Day 31 - DBMS Project

FILE_NAME = "student_records.txt"


def load_records():

    records = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:

            data = line.strip().split(",")

            records.append(data)

        file.close()

    except:
        print("File not found!")

    return records


def display(records):

    print("\nRoll No | Name | Marks")
    print("-" * 30)

    for record in records:

        print(record[0], "|", record[1], "|", record[2])


def sort_by_marks(records):

    records.sort(key=lambda x: int(x[2]), reverse=True)

    print("\nRecords Sorted by Marks")

    display(records)


def sort_by_name(records):

    records.sort(key=lambda x: x[1])

    print("\nRecords Sorted by Name")

    display(records)

