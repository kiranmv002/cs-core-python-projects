# Inventory Management System
# Day 35 - Academic Project

FILE_NAME = "inventory.txt"


def add_product():

    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    quantity = input("Enter Quantity: ")
    price = input("Enter Price: ")

    file = open(FILE_NAME, "a")
    file.write(pid + "," + name + "," + quantity + "," + price + "\n")
    file.close()

    print("Product added successfully!")


def view_products():

    try:
        file = open(FILE_NAME, "r")

        print("\nID | Product | Quantity | Price")
        print("-" * 40)

        for line in file:

            data = line.strip().split(",")

            print(data[0], "|", data[1], "|", data[2], "|", data[3])

        file.close()

    except:
        print("Inventory file not found!")


def search_product():

    pid = input("Enter Product ID: ")

    found = False

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        if data[0] == pid:

            print("\nProduct Found")
            print("ID:", data[0])
            print("Name:", data[1])
            print("Quantity:", data[2])
            print("Price:", data[3])

            found = True
            break

    file.close()

    if not found:
        print("Product not found!")
