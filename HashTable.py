from Rb_Tree import Rb_Tree
from Data_Structure import Structure
from hList import hList


class Hash(Structure):
    def __init__(self, n):
        super(Structure, self).__init__()
        self.hash_table = [hList() for _ in range(1000)]
        self.transition = n
        self.comparisons = 0

    def get_hmap(self):
        return self.hash_table

    def hashing(self, key_value):
        return key_value % len(self.hash_table)

    def insert(self, value):
        try:
            key_value = sum([ord(c) for c in value])
        except TypeError:
            key_value = value

        hash_key = self.hashing(key_value)
        self.hash_table[hash_key].insert(value)

        if type(self.hash_table[hash_key]) is hList:
            if len(self.hash_table[hash_key].get_list()) > self.transition:
                rb_tree = Rb_Tree()
                for element in self.hash_table[hash_key].get_list():
                    rb_tree.insert(element)
                self.hash_table[hash_key] = rb_tree

    # def display_hash(self):
    #     for element in self.hash_table:
    #         element.print()

    def find(self, value):
        try:
            key_value = sum([ord(c) for c in value])
        except TypeError:
            key_value = value

        hash_key = self.hashing(key_value)
        self.hash_table[hash_key].find(value)
        self.comparisons = self.hash_table[hash_key].bundle()

    def delete(self, value):
        try:
            key_value = sum([ord(c) for c in value])
        except TypeError:
            key_value = value

        hash_key = self.hashing(key_value)
        self.hash_table[hash_key].delete(value)

    def inorder(self):
        print("\n")

    def min(self):
        print("\n")

    def max(self):
        print("\n")

    def successor(self, x):
        print("\n")

    def load(self, f):
        for value in open(f, "r").read().split():
            self.insert(value)
