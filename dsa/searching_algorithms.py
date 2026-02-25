# Searching Algorithms Implementation
# Day 16 - Data Structures Project


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    arr = list(map(int, input("Enter sorted numbers (space separated): ").split()))

    print("\nChoose Searching Algorithm:")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = input("Enter choice: ")
    key = int(input("Enter number to search: "))

    if choice == "1":
        result = linear_search(arr, key)
        if result != -1:
            print(f"Element found at index {result}")
        else:
            print("Element not found!")

    elif choice == "2":
        result = binary_search(arr, key)
        if result != -1:
            print(f"Element found at index {result}")
        else:
            print("Element not found!")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
