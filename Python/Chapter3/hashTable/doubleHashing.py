import random


class HashTable:
    """Using Linear Probing."""
    
    def __init__(self):
        self.size = 20
        self.hash_table = [None] * self.size

    def another_hash(self, x):
        return (3 * x) % self.size

    def insert(self, data):
        initial_index = hash(data) % self.size
        index2 = self.another_hash(data)
        index = initial_index
        while self.hash_table[index]:
            index = (index + index2) % self.size
            # If hashtbale is full double the size
            if index == initial_index:
                self.hash_table += [None] * self.size
                self.size += self.size
        self.hash_table[index] = data

    def search(self, data):
        index = hash(data) % self.size
        index2 = self.another_hash(data)
        if self.hash_table[index] == data:
            print(f"{data} found!")
            return
        while self.hash_table[index] != data and self.hash_table[index] is not None:
            index = (index + index2) % self.size
        if self.hash_table[index] == data:
            print(f"{data} found!")
            return
        else:
            raise KeyError(f"{data} does not exist in the hash table.")


if __name__ == "__main__":
    ht = HashTable()
    for _ in range(25):
        ht.insert(random.randint(0, 100))
    try:
        ht.search(333)
    except KeyError as err:
        print(err)
    try:
        ht.search(5)
    except KeyError as err:
        print(err)
    print(ht.size)