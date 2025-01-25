from dataStructures.Linear.LinkedList import LinkedList


class HashChain:

    def __init__(self):
        self.hash_table_size = 10
        self.hash_table = [0] * self.hash_table_size
        for i in range(self.hash_table_size):
            self.hash_table[i] = LinkedList()

    def hashcode(self, key):
        return key % self.hash_table_size

    def insert(self, element):
        i = self.hashcode(element)
        self.hash_table[i].insert_sorted(element)

    def search(self, key):
        i = self.hashcode(key)
        return self.hash_table[i].search(key) != -1

    def display(self):
        for i in range(self.hash_table_size):
            print('[', i, ']', end=' ')
            self.hash_table[i].display()
        print()


if __name__ == '__main__':
    hash_chain = HashChain()
    hash_chain.insert(54)
    hash_chain.insert(78)
    hash_chain.insert(64)
    hash_chain.insert(92)
    hash_chain.display()
