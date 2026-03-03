# Bank Management System
# Simple File-Based Implementation

FILE_NAME = "bank_accounts.txt"


def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = input("Enter Initial Balance: ")

    with open(FILE_NAME, "a") as file:
        file.write(acc_no + "," + name + "," + balance + "\n")

    print("Account created successfully!\n")


def view_accounts():
    try:
        file = open(FILE_NAME, "r")
        print("\nAccount No | Name | Balance")
        print("--------------------------------")

        for line in file:
            data = line.strip().split(",")
            print(data[0], "|", data[1], "|", data[2])

        file.close()

    except:
        print("No accounts found!\n")


def deposit_money():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter amount to deposit: "))

    updated = False
    new_data = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split(",")

            if data[0] == acc_no:
                balance = float(data[2])
                balance += amount
                data[2] = str(balance)
                updated = True

            new_data.append(",".join(data) + "\n")

        file.close()

        file = open(FILE_NAME, "w")
        file.writelines(new_data)
        file.close()

        if updated:
            print("Amount deposited successfully!\n")
        else:
            print("Account not found!\n")

    except:
        print("Error while depositing!\n")


def withdraw_money():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter amount to withdraw: "))

    updated = False
    new_data = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split(",")

            if data[0] == acc_no:
                balance = float(data[2])

                if balance >= amount:
                    balance -= amount
                    data[2] = str(balance)
                    updated = True
                else:
                    print("Insufficient balance!\n")
                    return

            new_data.append(",".join(data) + "\n")

        file.close()

        file = open(FILE_NAME, "w")
        file.writelines(new_data)
        file.close()

        if updated:
            print("Amount withdrawn successfully!\n")
        else:
            print("Account not found!\n")

    except:
        print("Error while withdrawing!\n")


# ---------------- Main Menu ----------------

while True:
    print("------ Bank Management System ------")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        deposit_money()

    elif choice == "4":
        withdraw_money()

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!\n")
