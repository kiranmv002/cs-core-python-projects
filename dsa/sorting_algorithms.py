# Sorting Algorithms Implementation
# Day 14 - Data Structures Project


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def main():
    arr = list(map(int, input("Enter numbers (space separated): ").split()))

    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = input("Enter choice: ")

    if choice == "1":
        sorted_arr = bubble_sort(arr)
        print("Sorted using Bubble Sort:", sorted_arr)

    elif choice == "2":
        sorted_arr = selection_sort(arr)
        print("Sorted using Selection Sort:", sorted_arr)

    elif choice == "3":
        sorted_arr = insertion_sort(arr)
        print("Sorted using Insertion Sort:", sorted_arr)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
