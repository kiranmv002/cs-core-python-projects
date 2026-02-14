# Page Replacement Simulator
# Day 7 - Operating Systems Project
# Algorithms: FIFO and LRU


def fifo(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1

    print("\nFIFO Page Faults:", page_faults)


def lru(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_page = memory[0]
                min_index = pages.index(lru_page)
                for m in memory:
                    if pages.index(m) < min_index:
                        min_index = pages.index(m)
                        lru_page = m
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        else:
            memory.remove(page)
            memory.append(page)

    print("LRU Page Faults:", page_faults)


def main():
    pages = list(map(int, input("Enter page reference string (space separated): ").split()))
    capacity = int(input("Enter number of frames: "))

    print("\nChoose Algorithm:")
    print("1. FIFO")
    print("2. LRU")

    choice = int(input("Enter choice: "))

    if choice == 1:
        fifo(pages, capacity)
    elif choice == 2:
        lru(pages, capacity)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
