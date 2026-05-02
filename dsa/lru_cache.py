# LRU Cache Simulation
# Day 24 - Data Structures Project

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def access_page(self, page):

        if page in self.cache:
            print(f"Page {page} -> HIT")
            self.cache.remove(page)
            self.cache.append(page)

        else:
            print(f"Page {page} -> MISS")

            if len(self.cache) >= self.capacity:
                removed = self.cache.pop(0)
                print(f"Removed least recently used page: {removed}")

            self.cache.append(page)

        print("Current Cache:", self.cache)


# -------- MAIN --------

capacity = int(input("Enter cache size: "))
lru = LRUCache(capacity)

pages = input("Enter page reference string (space separated): ").split()

for page in pages:
    lru.access_page(page)
