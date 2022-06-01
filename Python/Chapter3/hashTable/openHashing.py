class HashTable:
    """Using Open Hashing."""
    
    def __init__(self):
        self.size = 20
        self.hash_table = [[] for _ in range(self.size)]

    def insert(self, data):
        index = hash(data) % self.size
        self.hash_table[index].append(data)

    def search(self, data):
        index = hash(data) % self.size
        for element in self.hash_table[index]:
            if element == data:
                print(f"{data} found!")
                return
        raise KeyError(f"{data} does not exist in the hash table.")


if __name__ == "__main__":
    ht = HashTable()
    ht.insert(2)
    ht.insert(23)
    ht.insert(5)
    ht.insert(4)
    ht.insert(3)
    ht.search(5)
    try:
        ht.search(333)
    except KeyError as err:
        print(err)
