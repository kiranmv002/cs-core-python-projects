# Bank Management System
# Day 18 - Academic Project

FILE_NAME = "bank_accounts.txt"


def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{acc_no},{name},{balance}\n")

    print("Account created successfully!")


def view_accounts():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nAcc No | Name | Balance")
            print("-" * 30)
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                print(f"{acc_no} | {name} | {balance}")
    except FileNotFoundError:
        print("No accounts found!")


def deposit():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Amount to Deposit: "))
    updated = False
    records = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                a_no, name, balance = line.strip().split(",")
                if a_no == acc_no:
                    balance = str(float(balance) + amount)
                    updated = True
                records.append(f"{a_no},{name},{balance}\n")

        with open(FILE_NAME, "w") as file:
            file.writelines(records)

        if updated:
            print("Amount deposited successfully!")
        else:
            print("Account not found!")

    except FileNotFoundError:
        print("No accounts found!")
