# Page Replacement Simulator
# Day 8 Upgrade: Added Optimal + Frame Display


def display_frames(frames):
    print("Frames:", frames)


def fifo(pages, capacity):
    frames = []
    page_faults = 0

    print("\nFIFO Execution:")

    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
            print(f"Page {page} -> Fault")
        else:
            print(f"Page {page} -> Hit")

        display_frames(frames)

    print("Total FIFO Page Faults:", page_faults)


def lru(pages, capacity):
    frames = []
    page_faults = 0

    print("\nLRU Execution:")

    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
            print(f"Page {page} -> Fault")
        else:
            frames.remove(page)
            frames.append(page)
            print(f"Page {page} -> Hit")

        display_frames(frames)

    print("Total LRU Page Faults:", page_faults)


def optimal(pages, capacity):
    frames = []
    page_faults = 0

    print("\nOptimal Execution:")

    for i in range(len(pages)):
        page = pages[i]

        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i+1:]
                index_list = []

                for frame_page in frames:
                    if frame_page in future:
                        index_list.append(future.index(frame_page))
                    else:
                        index_list.append(float('inf'))

                replace_index = index_list.index(max(index_list))
                frames[replace_index] = page

            page_faults += 1
            print(f"Page {page} -> Fault")
        else:
            print(f"Page {page} -> Hit")

        display_frames(frames)

    print("Total Optimal Page Faults:", page_faults)


def main():
    pages = list(map(int, input("Enter page reference string (space separated): ").split()))
    capacity = int(input("Enter number of frames: "))

    print("\nChoose Algorithm:")
    print("1. FIFO")
    print("2. LRU")
    print("3. Optimal")

    choice = int(input("Enter choice: "))

    if choice == 1:
        fifo(pages, capacity)
    elif choice == 2:
        lru(pages, capacity)
    elif choice == 3:
        optimal(pages, capacity)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
